"use client";
import {useRouter} from "next/navigation";
export default function CatalogueFilters({categories,search,category,sort,base,from}){
 const router=useRouter();
 function navigate(event){event.preventDefault();const data=new FormData(event.currentTarget);const params=new URLSearchParams();for(const key of ["search","category","sort"]){const value=String(data.get(key)||"").trim();if(value && !(key==="sort"&&value==="default"))params.set(key,value)}if(from)params.set("from",from);router.push(`${base}${params.size?`?${params}`:""}`)}
 return <form className="catalogue-filters" onSubmit={navigate}><label>Search products<input name="search" type="search" defaultValue={search} maxLength={100}/></label><label>Category<select name="category" defaultValue={category}><option value="">All categories</option>{categories.map(c=><option key={c.slug} value={c.slug}>{c.name}</option>)}</select></label><label>Sort by<select name="sort" defaultValue={sort}><option value="default">Featured</option><option value="name">Name A-Z</option><option value="price-asc">Price: low to high</option><option value="price-desc">Price: high to low</option></select></label><button className="button primary" type="submit">Apply filters</button></form>
}
