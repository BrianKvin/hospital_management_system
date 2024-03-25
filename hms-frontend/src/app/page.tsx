import Footer from "@/components/landing/footer";
import NavBar from "@/components/landing/navbar";
import { Button } from "@/components/ui/button";
import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Button variant='destructive' >Click Me!</Button>
      <NavBar />
      <Footer />
    </main>
  );
}
