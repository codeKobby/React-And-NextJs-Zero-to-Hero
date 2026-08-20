import { useState } from 'react'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <main>
      <h1>React playground</h1>
      <p>Clicked {count} times.</p>
      <button type="button" onClick={() => setCount((current) => current + 1)}>
        Increment
      </button>
    </main>
  )
}
