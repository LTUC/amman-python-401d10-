import Link from 'next/link.js';


export default function Footer() {
    return (
        <footer className="flex justify-between p-4 mt-8 bg-gray-500 text-gray-50">
            <p>&copy; ASAC Team</p>
            <Link href="/careers">Careers</Link>
        </footer>
    )
}
