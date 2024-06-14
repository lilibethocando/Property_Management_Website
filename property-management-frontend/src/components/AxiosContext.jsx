import React, { createContext } from 'react';
import axios from 'axios';

const AxiosContext = createContext();

const axiosInstance = axios.create({
    baseURL: process.env.NODE_ENV === 'production' ? 'https://property-management-website.onrender.com' : 'http://localhost:5000',
    withCredentials: true,
});

const AxiosProvider = ({ children }) => {
    return (
        <AxiosContext.Provider value={axiosInstance}>
            {children}
        </AxiosContext.Provider>
    );
};

export { AxiosProvider, AxiosContext };
