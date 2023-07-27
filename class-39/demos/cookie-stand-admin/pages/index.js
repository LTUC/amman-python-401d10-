import Head from 'next/head';
import {useAuth} from "../contexts/auth";
import useResource from '../hooks/useResource';

export default function Home() {

    const {login, user, logout} = useAuth(); 
    const {resource, loading, createResource, deleteResource} = useResource();

    // const user = {username:"roaa", password:"roaa"};
    // send req to server -> tokens

    return (
        <div>
            <Head>
                <title>Cookie Stand Demo</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                
                {user ? (
                    <>
                    <button className="p-2 text-white bg-gray-500 rounded" onClick={()=>logout()}>Logout</button>
                    <h2>Welcome {user.username}</h2>
                    <CreateForm onCreate={createResource}/>
                    <StandList data={resource} loading={loading} onDelete={deleteResource}/>
                    </>
                ) : (
                    <>
                    <button className="p-2 text-white bg-gray-500 rounded" onClick={()=>login("toqa","toqa2121")}>Login</button>
                    <h2>Need to log in</h2>
                    </>
                )}
            </main>
        </div>
    )
}

function StandList({data, loading, onDelete}) {

    if(loading) return <p>Loading ...</p>
    return(
        <>
         <h3 className="text-xl">Cookies Stand List</h3>
        {data.map(item =>(
            <li key={item.id}>
                <span>{item.location}</span>
                <span onClick={() => onDelete(item.id)}>[X]</span>
            </li>
        ))}

        </>
    )
}


function CreateForm({onCreate}){

    function handleSubmit(event) {
        event.preventDefault();
        const standInfo = {
            location : event.target.location.value,
            minimum_customers_per_hour : event.target.min.value,
            maximum_customers_per_hour : event.target.max.value,
            average_cookies_per_sale : event.target.avg.value 
        }
        onCreate(standInfo)
    }
    return (
        <>
            <h3 className="text-xl"> Create new item</h3>
            <form onSubmit={handleSubmit}>
                <input className="border border-black" name="location" placeholder='Location'/>
                <input className="border border-black" name="min" placeholder='min'/>
                <input className="border border-black" name="max" placeholder='max'/>
                <input className="border border-black" name="avg" placeholder='avg'/>
                <button className="p-2 bg-gray-500 text-white">Create</button>
            </form>
        </>
    )
}