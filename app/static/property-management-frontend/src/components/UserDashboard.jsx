import React from 'react';
import { useState } from 'react';
import '../index.css'


const UserDashboard = ({ rentAmount, contractDuration }) => {
    const [complaint, setComplaint] = useState('');
    const [request, setRequest] = useState('');
    const [reminder, setReminder] = useState('');
    const [email, setEmail] = useState('');

    return (
        <div className="dashboard">
            <h1>Welcome to the User Dashboard!</h1>
            <p>Rent Amount: {rentAmount}</p>
            <p>Contract Duration: {contractDuration} months</p>

            <div className="complaint-section">
                <h2>Make a Complaint</h2>
                <select onChange={(e) => setComplaint(e.target.value)}>
                    <option value="">Select complaint...</option>
                    {/* Add your complaint options here */}
                </select>
                <textarea placeholder="Write your complaint here..."></textarea>
                <button>Upload Picture</button>
            </div>

            <div className="request-section">
                <h2>Make a Request</h2>
                <select onChange={(e) => setRequest(e.target.value)}>
                    <option value="">Select request...</option>
                    {/* Add your request options here */}
                </select>
                <textarea placeholder="Write your request here..."></textarea>
            </div>

            <div className="reminder-section">
                <h2>Set a Reminder</h2>
                <input type="date" onChange={(e) => setReminder(e.target.value)} />
            </div>

            <div className="email-section">
                <h2>Send an Email</h2>
                <input type="email" placeholder="Email address" onChange={(e) => setEmail(e.target.value)} />
                <textarea placeholder="Write your email here..."></textarea>
            </div>

            <div className="payment-section">
                <h2>Make a Payment</h2>
                <button>Pay Now</button>
                <h2>Payment History</h2>
                {/* Display payment history here */}
            </div>
        </div>
    );
};

export default UserDashboard;

