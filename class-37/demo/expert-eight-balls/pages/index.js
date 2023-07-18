import Head from 'next/head';
import {useState} from 'react';
import {replies} from '../data.js'

export default function Home() {

  const [question, setQuestion] = useState("Ask me anything ...")
  const [answer, setAnswer] = useState("Answer ...")

  function questionHandler(event){
    event.preventDefault();
    setQuestion(event.target.question.value)
    const randomReply = replies[Math.floor(Math.random() * replies.length)];
    setAnswer(randomReply)

    
  }  

  return (
    <>
      <Head>
        <title>Expert Eight Balls</title>
      </Head>
      <body>
        {/* Header */}
        <Header />
        <main className='flex flex-col items-center py-4 space-y-8'>
          {/* form */}
          <Form handler={questionHandler}/>

          {/* question section */}
          <Question question={question}/>

          <p className="text-4xl text-center">{answer}</p>

        </main>
        <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
          &copy; ASAC Team
        </footer>
      </body>
    </>
  )
}

function Header() {
  return (
    <header className='flex items-center justify-between p-4 bg-gray-500 text-gray-50'>
      <h1 className='text-4xl'>Expert 8 balls</h1>
      <p>1 questions answered</p>
    </header>
  )
}

function Form(props) {
  return (
    <form className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200" onSubmit={props.handler}>
      <input name="question" className="flex-auto pl-1" />
      <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
    </form>
  )
}

function Question(props) {
  return (
    <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
      <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
        <p className="text-xl text-center">{props.question}</p>
      </div>
    </div>
  )
}