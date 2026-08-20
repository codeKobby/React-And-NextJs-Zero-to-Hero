import { Button } from '@/components/ui/button';

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-slate-50 px-6 py-12 text-slate-950 sm:px-10">
      <section className="mx-auto max-w-3xl rounded-2xl border border-slate-200 bg-white p-8 shadow-sm">
        <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Protected route fixture</p>
        <h1 className="mt-2 text-3xl font-bold tracking-tight">Synthetic dashboard</h1>
        <p className="mt-3 text-slate-600">
          This route is matched by <code className="rounded bg-slate-100 px-1.5 py-0.5 text-sm">proxy.ts</code>.
          The proxy redirect is only an optimistic check; real applications must authorize data and mutations on the server.
        </p>
        <Button className="mt-6" variant="outline" type="button">Review route boundary</Button>
      </section>
    </main>
  );
}
