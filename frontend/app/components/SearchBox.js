"use client";
import { useRouter } from "next/navigation";
export default function SearchBox() {
  const router = useRouter();
  function submit(event) {
    event.preventDefault();
    const query = String(new FormData(event.currentTarget).get("search") || "").trim();
    const params = new URLSearchParams();
    if (query) params.set("search", query);
    const current = window.location.pathname + window.location.search;
    if (window.location.pathname !== "/search" && current.length <= 1000) params.set("from", current);
    router.push(`/search?${params}`);
  }
  return <form className="search-wrap" action="/search" onSubmit={submit}><label htmlFor="site-search" className="sr-only">Search products</label><span aria-hidden="true">⌕</span><input id="site-search" name="search" type="search" placeholder="Search groceries and more" maxLength={100}/><button type="submit">Search</button></form>;
}
