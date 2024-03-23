import { useEffect, useState } from 'react'

export default async function Home() {
  const res = await fetch('http://localhost:5000/test', { cache: 'no-store' })
  const data = await res.json()

  console.log(data)

  return (
    <main className='flex min-h-screen flex-col items-center justify-between p-24'>
      <h1 className='text-4xl font-bold'>Welcome to WealthWise</h1>

      <h2>{data.message}</h2>
    </main>
  )
}
