import React, { useState } from 'react';
import axios from 'axios';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('pk_test_51OCsCqCb8MXdJtc6zbhHL9pJ8ceF8cLFbYy9sMfMa9hjwMbKpHtvuxE7rzSGmeXSRvO01t23heGuZSjAqH33AXk800gQ5oB94T');

const MakePayment = () => {
    const [tenantId, setTenantId] = useState('');
    const [amount, setAmount] = useState('');
    const [paymentMethod, setPaymentMethod] = useState('');
    const [paymentId, setPaymentId] = useState('');
    const [balance, setBalance] = useState('');
    const [showPaymentDetails, setShowPaymentDetails] = useState(false);
    const [showEmailInput, setShowEmailInput] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handlePayment = async () => {
        setLoading(true);
        try {
            let paymentData;
            
            // Send OPTIONS request first
            await axios.options('http://localhost:5000/payments/makepayment');
    
            // Then send the POST request
            const response = await axios.post('http://localhost:5000/payments/makepayment', {
                tenant_id: tenantId,
                amount: amount,
                payment_method: paymentMethod,
                description: 'Rent payment'
            });
            
            paymentData = response.data;

            // Update UI based on payment method
            if (paymentMethod === 'Stripe') {
                // Show payment details from Stripe response
                setPaymentId(paymentData.payment_id);
                setBalance(paymentData.balance);
                setShowPaymentDetails(true);
            } else {
                // Show basic payment details
                setPaymentId(paymentData.payment_id);
                setShowPaymentDetails(true);
            }

            setLoading(false); // Update loading state after payment processing
        } catch (error) {
            setError('Error making payment: ' + error.message);
            setLoading(false);
        }
    };
    

    const handleChange = (e) => {
        setPaymentMethod(e.target.value);
    };

    const handleEmailSubmit = () => {
        // Logic for sending email
    };

    return (
        <div className="container mx-auto flex justify-center items-center h-screen mt-20 mb-20">
            <div className="bg-white rounded-lg shadow-md p-10">
                <h1 className="text-3xl font-semibold mb-6 text-center">Make Payment</h1>
                <div className="mb-4">
                    <label htmlFor="tenantId" className="block font-semibold mb-2">Tenant ID:</label>
                    <input
                        type="text"
                        id="tenantId"
                        className="border border-gray-300 rounded px-4 py-2 w-full"
                        value={tenantId}
                        onChange={(e) => setTenantId(e.target.value)}
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="amount" className="block font-semibold mb-2">Amount:</label>
                    <input
                        type="text"
                        id="amount"
                        className="border border-gray-300 rounded px-4 py-2 w-full"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                </div>
                <div className="mb-4">
                    <label htmlFor="paymentMethod" className="block font-semibold mb-2">Payment Method:</label>
                    <select
                        id="paymentMethod"
                        className="border border-gray-300 rounded px-4 py-2 w-full"
                        value={paymentMethod}
                        onChange={handleChange}
                    >
                        <option value="">Select Payment Method</option>
                        <option value="Stripe">Stripe</option>
                        <option value="Check">Check</option>
                        <option value="Zelle">Zelle</option>
                    </select>
                </div>
                <button
                    className="bg-blue-500 text-white font-semibold py-2 px-6 rounded disabled:opacity-50 block mx-auto"
                    onClick={handlePayment}
                    disabled={!tenantId || !amount || !paymentMethod || loading}
                >
                    {loading ? 'Processing...' : 'Pay'}
                </button>
                {showPaymentDetails && (
                    <div className="mt-8">
                        <h2 className="text-xl font-semibold mb-4">Payment Details</h2>
                        <p><strong>Payment ID:</strong> {paymentId}</p>
                        <p><strong>Amount:</strong> ${amount}</p>
                        <p><strong>New Balance:</strong> ${balance}</p>
                    </div>
                )}
                {showEmailInput && (
                    <div className="mt-8">
                        <h2 className="text-xl font-semibold mb-4">Send Payment Details via Email</h2>
                        <div className="mb-4">
                            <label htmlFor="email" className="block font-semibold mb-2">Email:</label>
                            <input
                                type="email"
                                id="email"
                                className="border border-gray-300 rounded px-4 py-2 w-full"
                            />
                        </div>
                        <button
                            className="bg-blue-500 text-white font-semibold py-2 px-6 rounded block mx-auto"
                            onClick={handleEmailSubmit}
                        >
                            Send Email
                        </button>
                    </div>
                )}
                {error && <p className="text-red-500 mt-4">{error}</p>}
            </div>
        </div>
    );
};

export default MakePayment;
