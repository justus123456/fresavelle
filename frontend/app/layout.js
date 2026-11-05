import "./globals.css";
import {Header,Footer} from "./components/Storefront";
export const metadata={title:"Fresavelle | Fresh food for the way you live",description:"A first look at Fresavelle, an Abuja grocery experience."};
export default function RootLayout({children}){return <html lang="en"><body><Header/>{children}<Footer/></body></html>}
