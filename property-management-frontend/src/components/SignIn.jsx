import React, { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // Import useNavigate
import '../index.css'; // Import the CSS file for styling
import { AxiosContext } from './AxiosContext'; // Import AxiosContext

export default function SignIn() {
    const axiosInstance = useContext(AxiosContext); // Use axios instance from context
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate(); // Use useNavigate for programmatic navigation

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axiosInstance.post('/signin', formData); // Use axiosInstance
            console.log(response.data);
            localStorage.setItem('token', response.data.token); // Store token in localStorage
            setErrorMessage(''); // Clear any previous errors
            
            // Redirect based on user's is_admin status
            if (response.data.is_admin) {
                navigate('/AdminDashboard'); // Redirect to Admin Dashboard
            } else {
                navigate('/UserDashboard'); // Redirect to User Dashboard
            }
        } catch (error) {
            console.error(error.response.data);
            setErrorMessage(error.response.data.message);
        }
    };

    return (
        <div className="max-w-md mx-auto mt-20">
            <h1 className="text-2xl font-bold text-center mb-6">Sign In</h1>
            <form onSubmit={handleSubmit}>
                <div className="mb-4">
                    <label htmlFor="email" className="block text-sm font-bold mb-1">Email</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="Enter your email address"
                        required
                        className="w-full border border-gray-300 rounded-md py-2 px-3"
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="password" className="block text-sm font-bold mb-1">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="Enter your password"
                        required
                        className="w-full border border-gray-300 rounded-md py-2 px-3"
                    />
                </div>
                <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Sign In</button>
            </form>
            {errorMessage && <p className="text-red-500">{errorMessage}</p>}
            <p className="mt-4 text-sm">Don't have an account? <Link to="/signup" className="text-blue-500">Sign Up</Link></p>
        </div>
    );
}
