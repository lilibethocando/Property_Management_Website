import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';  // Import useHistory

const SignUp = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });

    const [successMessage, setSuccessMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const history = useHistory();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/signup', formData);
            console.log(response.data);
            setSuccessMessage('You have successfully signed up!');
            setErrorMessage(''); // Clear any previous errors
            history.push('/success');  // Navigate to success page route
        } catch (error) {
            console.error(error.response.data);
            setSuccessMessage(''); // Clear any previous success messages
            setErrorMessage(error.response.data.message);
        }
    };

    return (
        <div className="max-w-md mx-auto mt-20">
            <h1 className="text-2xl font-bold text-center mb-6">Sign Up</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                />
                <button type="submit">Sign Up</button>
            </form>
            {successMessage && <p className="text-green-500">{successMessage}</p>}
            {errorMessage && <p className="text-red-500">{errorMessage}</p>}
        </div>
    );
};

export default SignUp;
