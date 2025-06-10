import React  from 'react'
import Navbar from "../navbar/Navbar"

interface Container{
    children: React.ReactNode;
}


function Layout({children}: Container) {
  return (
    <>
        <Navbar />
            {children}

    </>
    
  )
}
export default Layout