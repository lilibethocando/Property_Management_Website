import { Menu, X } from 'lucide-react';
import { useState } from 'react';
import logo from '../assets/smart_property_logo.jpg';
import { navItems } from '../constants';

const Navbar = () => {
    const handleClick = (e) => {
        e.preventDefault();
        alert('Sign In clicked');
    }

    const [mobileDrawerOpen, setMobileDrawerOpen] = useState(false);
        const toggleNavbar = () => {
            setMobileDrawerOpen(!mobileDrawerOpen);
        }


    return (
        <nav className="nav.sticky.top-0.z-50.py-3.backdrop-blur-lg.border-b.border-neutral-700/80">
            <div className="container px-4 mx-auto relative text-sm">
                <div className="flex justify-between items-center">
                    <div className="flex items-center flex-shrink-0">
                        <img className="h-12 w-12 mr-2" src={logo} alt="Company Logo"/>
                        <span className="text-xl tracking-tight">SPP</span>
                    </div>
                    <ul className='hidden lg:flex ml-14 space-x-12'>
                        {navItems.map((item, index) => (
                            <li key={index}>
                                <a href={item.href}>{item.label}</a>
                            </li>
                        ))}
                    </ul>
                    <div className="hidden lg:flex justify-center space-x-12 items-center">
                        <a href="#!" onClick={handleClick} className='py-2 px-3 border rounded-md' >
                            Sign In
                            </a>
                        <a href="#!" className='bg-gradient-to-r from-green-400 to-green-200 py-2 px-3 rounded-md'>
                            Sign Up
                            </a>
                    </div>
                    <div className="lg:hidden md:flex flex-col justify-end">
                        <button onClick={toggleNavbar}>
                            {mobileDrawerOpen ? <X size={24} /> : <Menu size={24} />}
                        </button>
                    </div>
                </div>
                {mobileDrawerOpen && (  
                    <div className="fixed right-0 z-20 bg-neutral-900 w-full p-12 flex flex-col justify-center items-center lg:hidden">
                        <ul>
                            
                        </ul>
                    </div>
                    )}
            </div>
        </nav>
    )
}

export default Navbar