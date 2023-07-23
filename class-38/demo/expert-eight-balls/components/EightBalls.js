export default function EightBalls(props) {
    return (
      <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          <p className="text-xl text-center">{props.answer || "Waiting ..."}</p>
        </div>
      </div>
    )
  }