import Head from 'next/head';
import { useState } from 'react';
import { replies } from '../data.js';

import Header from '../components/Header.js';
import Form from '../components/Form.js';
import Footer from '../components/Footer.js';
import EightBalls from '../components/EightBalls.js';
import History from '../components/History.js';


export default function Home() {

  const [questions, setQuestions] = useState([])
  // const [answer, setAnswer] = useState("Answer ...")

  function questionHandler(event) {
    event.preventDefault();
    // setQuestion(event.target.question.value)
    const randomReply = replies[Math.floor(Math.random() * replies.length)];
    // setAnswer(randomReply)
    //new code
    const questionObj = {
      id : questions.length +1 ,
      question : event.target.question.value,
      answer : randomReply
    }

    setQuestions([...questions,questionObj]) // create new array
    // questions[questions.length] = questionObj
  }

  function getAswer(){
    if (questions.length == 0){
      return "";
    }
    else{
      return questions[questions.length -1 ].answer
    }
    
  }

  return (
    <>
      <Head>
        <title>Expert Eight Balls</title>
      </Head>
      {/* Header */}
      <Header questionsLength={questions.length}/>
      <main className='flex flex-col items-center py-4 space-y-8'>
        {/* form */}
        <Form handler={questionHandler} />

        {/* question section */}
        <EightBalls answer={getAswer()} />

        {/* <p className="text-4xl text-center">{answer}</p> */}
        <History questionsList={questions}/>

      </main>
      <Footer />
    </>
  )
}

