export function ListingSkeleton() {
  return <main className="wrap listing" id="main" aria-busy="true">
    <p className="loading-message" role="status">Loading products...</p>
    <div aria-hidden="true">
      <div className="skeleton skeleton-heading"/><div className="skeleton skeleton-caption"/>
      <div className="skeleton-filters"><div className="skeleton"/><div className="skeleton"/><div className="skeleton"/></div>
      <div className="product-grid listing-grid">{[0,1,2,3].map((item)=><div className="skeleton-card" key={item}><div className="skeleton skeleton-image"/><div className="skeleton skeleton-line"/><div className="skeleton skeleton-line short"/><div className="skeleton skeleton-price"/></div>)}</div>
    </div>
  </main>;
}
export function ProductSkeleton() {
  return <main className="wrap listing" id="main" aria-busy="true">
    <p className="loading-message" role="status">Loading product...</p>
    <div className="product-detail" aria-hidden="true"><div className="skeleton skeleton-detail-image"/><div><div className="skeleton skeleton-caption"/><div className="skeleton skeleton-heading"/><div className="skeleton skeleton-line"/><div className="skeleton skeleton-line short"/><div className="skeleton skeleton-price"/></div></div>
  </main>;
}
