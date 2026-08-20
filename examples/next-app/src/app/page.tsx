import { Button } from '@/components/ui/button';
import Counter from '@/components/interactive/Counter';

const syntheticCases = [
  { id: 'case-001', title: 'Review access policy', status: 'Open' },
  { id: 'case-002', title: 'Test recovery flow', status: 'Pending' },
];

export default function Page() {
  return (
    <main className="min-h-screen bg-slate-50 px-6 py-12 text-slate-950 sm:px-10">
      <div className="mx-auto grid max-w-5xl gap-8">
        <header className="flex flex-col gap-4 rounded-2xl border border-slate-200 bg-white p-8 shadow-sm sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Local case desk</p>
            <h1 className="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">Modern React and Next.js</h1>
            <p className="mt-3 max-w-2xl text-slate-600">
              This page is a Server Component by default. It uses Tailwind CSS for layout and an owned UI primitive for the action.
            </p>
          </div>
          <Button type="button">Create synthetic case</Button>
        </header>

        <section aria-labelledby="cases-heading" className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="flex items-center justify-between gap-4">
            <div>
              <h2 id="cases-heading" className="text-xl font-semibold">Cases</h2>
              <p className="mt-1 text-sm text-slate-600">Invented data for learning; no external service is called.</p>
            </div>
            <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-700">{syntheticCases.length} records</span>
          </div>
          <ul className="mt-6 divide-y divide-slate-100">
            {syntheticCases.map((item) => (
              <li key={item.id} className="flex flex-col gap-2 py-4 sm:flex-row sm:items-center sm:justify-between">
                <span className="font-medium">{item.title}</span>
                <span className="text-sm text-slate-500">{item.status}</span>
              </li>
            ))}
          </ul>
        </section>

        <section aria-labelledby="counter-heading" className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <h2 id="counter-heading" className="text-xl font-semibold">Client interaction boundary</h2>
          <p className="mt-1 text-sm text-slate-600">Only the counter needs client-side state; the page remains a Server Component.</p>
          <div className="mt-4">
            <Counter />
          </div>
        </section>
      </div>
    </main>
  );
}
