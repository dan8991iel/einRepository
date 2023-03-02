import { asyncComputed } from '@vueuse/core';
import { useCurrentUser } from 'vuefire';

export type UserRole = 'customer' | 'sales' | 'admin';

export function useCurrentUserRole() {
  const user = useCurrentUser();

  return asyncComputed<UserRole>(async () => {
    const result = await user.value?.getIdTokenResult();
    return result?.claims?.role ?? 'customer';
  });
}