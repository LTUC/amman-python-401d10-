export default function History({ questionsList: questions }) {
    if (questions.length == 0) {
        return (
            <h3 className="w-1/2 mx-auto my-8 text-2xl text-center"> No questions have been asked :( </h3>
        )
    }
    else {
        return (
            <table className="w-1/2 mx-auto my-8 text-2xl text-center">
                <thead>
                    <tr>
                        <th className="border border-black">No.</th>
                        <th className="border border-black">Question</th>
                        <th className="border border-black">Response</th>
                    </tr>
                </thead>
                <tbody>
                    {questions.map(item => (
                        <tr>
                            <td className="border border-black">{item.id}</td>
                            <td className="border border-black">{item.question}</td>
                            <td className="border border-black">{item.answer}</td>
                        </tr>
                    ))

                    }
                </tbody>
            </table>
        )
    }
}