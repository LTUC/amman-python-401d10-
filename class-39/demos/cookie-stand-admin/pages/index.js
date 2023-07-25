import Head from 'next/head';
import {useAuth} from "../contexts/auth"

export default function Home() {

    const {login, user, logout} = useAuth(); 

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