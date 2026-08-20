import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// This is an optimistic navigation check for the local teaching fixture.
// The protected route and data layer must still perform authoritative authorization.
export function proxy(request: NextRequest) {
  const hasSyntheticSession = request.cookies.has('synthetic-session');

  if (!hasSyntheticSession) {
    return NextResponse.redirect(new URL('/', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
