'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div aria-labelledby="counter-heading" className="rounded-xl bg-slate-50 p-4">
      <h3 id="counter-heading" className="font-semibold">Client-side counter</h3>
      <p className="mt-1 text-sm text-slate-600">Clicked {count} times.</p>
      <button
        type="button"
        className="mt-3 rounded-md border border-slate-300 bg-white px-3 py-2 text-sm font-medium hover:bg-slate-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-500"
        onClick={() => setCount((current) => current + 1)}
      >
        Increment
      </button>
    </div>
  );
}
