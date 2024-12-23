import React, { useState } from 'react';
import './Navbar.css';

const NavBar = () => {
  const [openMenu,setOpenMenu] = useState(false);
  
  return (
    <header className="header">
      <a href="/" className="logo">LOGO</a>

      <nav className="navbar">
        <a href="/" className="home">Home</a>
        <a href="/about" className="about">About</a>
        <a href="/service" className="services">Services</a>
        <a href="/sign-up" className="sign up">Sign up</a>
      </nav>
    </header>
  );
}

export default NavBar;
