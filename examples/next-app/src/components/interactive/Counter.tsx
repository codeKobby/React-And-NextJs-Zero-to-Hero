'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <section aria-labelledby="counter-heading">
      <h2 id="counter-heading">Client-side counter</h2>
      <p>Clicked {count} times.</p>
      <button type="button" onClick={() => setCount((current) => current + 1)}>
        Increment
      </button>
    </section>
  )
}
