export default function Header({questionsLength}) {
    return (
      <header className='flex items-center justify-between p-4 bg-gray-500 text-gray-50'>
        <h1 className='text-4xl'>Expert 8 balls</h1>
        <p>{questionsLength} questions answered</p>
      </header>
    )
  }