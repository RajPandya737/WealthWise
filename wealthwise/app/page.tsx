import { useEffect, useState } from 'react'

export default async function Home() {
  const res = await fetch('http://localhost:5000/test', { cache: 'no-store' })
  const data = await res.json()

  console.log(data)

  return (
    <main className='flex min-h-screen flex-col items-center p-24'>
      <h1 className='text-4xl font-bold'>Welcome to WealthWise</h1>

      <div>
        <h2>{data.last_day}</h2>
        <h2>{data.week}</h2>
        <h2>{data.month}</h2>
        <h2>{data.three_months}</h2>
        <h2>{data.six_months}</h2>
        <h2>{data.year}</h2>
        <h2>{data.five_year}</h2>
      </div>
    </main>
  )
}
