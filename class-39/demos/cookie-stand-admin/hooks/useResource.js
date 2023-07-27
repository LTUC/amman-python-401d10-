import { useState } from "react";
import { useAuth } from "../contexts/auth";
import useSWR from 'swr';

export default function useResource() {

    const apiUrl = process.env.NEXT_PUBLIC_RESOURCE_URL;
    const {tokens, logout} = useAuth(); 
    const {data, error, mutate} = useSWR([apiUrl,tokens],fetchResource)


    async function fetchResource(){
        
        if (!tokens) {
            return;
        }

        try {
            const response = await fetch(apiUrl,config())
            const responseJSON = await response.json()
            console.log(responseJSON)
            return responseJSON;
        }
        catch(err){
            handleError(err);
        }
    }

    async function createResource(standInfo){
        if (!tokens) {
            return;
        }

        try {
            const options = config()
            options.method = "POST"
            options.body = JSON.stringify(standInfo)
            await fetch(apiUrl,options)
            mutate(); //collect the data again
        }
        catch(err){
            handleError(err);
        }
    }

    async function deleteResource(id){
        try {
            const url = apiUrl + id
            const options = config()
            options.method = "DELETE"
            await fetch(url, options)
            mutate(); //collect the data again
            
        }
        catch (err) {
            handleError(err); 
        }
    }

    function config(){
        return {
            headers : {
                'Content-Type' : 'application/json',
                'Authorization' : 'Bearer ' + tokens.access
            }
        }
    }

    function handleError(err) {
        console.log(err);
        logout();
    }

    return {
        resource : data,
        loading : tokens && !error && !data,
        createResource,
        deleteResource,
    }
}