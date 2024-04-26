import React, { useState } from 'react';
import { Card, Metric, Text, Button } from '@tremor/react';
import { Table, TableBody, TableCell, TableHead, TableHeaderCell, TableRow } from '@tremor/react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

import apt1 from '../assets/apt1.jpeg';
import apt2 from '../assets/apt2.webp';
import apt3 from '../assets/apt3.jpeg';

const UserDashboard = () => {
    // Fake data for apartments
    const apartments = [
        {
            name: 'Apartment 1',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 1,
            amenities: ['Swimming Pool', 'Gym', 'Parking'],
            rent: 1500,
            image: apt2
        },
        {
            name: 'Apartment 2',
            address: 'Chicago, IL',
            bedrooms: 3,
            bathrooms: 2,
            amenities: ['Balcony', 'Fitness Center', 'Laundry'],
            rent: 2000,
            image: apt1
        },
        {
            name: 'Apartment 3',
            address: 'Chicago, IL',
            bedrooms: 1,
            bathrooms: 1,
            amenities: ['Pet Friendly', 'Roof Deck', 'Utilities Included'],
            rent: 1200,
            image: apt3
        }
    ];

    const sliderSettings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        height: '300px' // Increase height for better display
    };

    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
    const currentDate = new Date().toLocaleDateString();

    const handleSendEmail = async () => {
        try {
            const response = await fetch('http://localhost:5000/sendemail', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, message })
            });
            if (response.ok) {
                console.log('Email sent successfully');
            } else {
                console.error('Failed to send email');
            }
        } catch (error) {
            console.error('Error sending email:', error);
        }
    };

    return (
        <div className="mx-auto max-w-2xl">
            <h1 className="text-3xl font-semibold mb-4 text-center mt-10">Units available at {currentDate}</h1>

            {/* Apartment Cards */}
            <div className="flex gap-4 justify-center">
                {apartments.map((apartment, index) => (
                    <Card key={index} className="max-w-xs bg-gray-100 bg-opacity-50" decoration="top" decorationColor="indigo">
                        <img src={apartment.image} alt={`Apartment ${index + 1}`} className="w-full h-40 object-cover" />
                        <div className="p-4">
                            <Text className="text-lg font-semibold">{apartment.name}</Text>
                            <Text className="text-sm">{apartment.address}</Text>
                            <div className="flex justify-between mt-2">
                                <Metric label="Bedrooms" value={apartment.bedrooms} />
                                <Metric label="Bathrooms" value={apartment.bathrooms} />
                                <Metric label="Rent" value={`$${apartment.rent}/month`} />
                            </div>
                            <div className="mt-2">
                                <Text className="font-semibold">Amenities:</Text>
                                <ul className="list-disc list-inside">
                                    {apartment.amenities.map((amenity, index) => (
                                        <li key={index}>{amenity}</li>
                                    ))}
                                </ul>
                            </div>
                        </div>
                    </Card>
                ))}
            </div>

            {/* Table */}
            <Table className="mt-8 bg-gray-100 bg-opacity-50 mx-auto">
                <TableHead>
                    <TableRow>
                        <TableHeaderCell>Name</TableHeaderCell>
                        <TableHeaderCell>Address</TableHeaderCell>
                        <TableHeaderCell>Bedrooms</TableHeaderCell>
                        <TableHeaderCell>Bathrooms</TableHeaderCell>
                        <TableHeaderCell>Amenities</TableHeaderCell>
                        <TableHeaderCell>Rent</TableHeaderCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {apartments.map((apartment, index) => (
                        <TableRow key={index}>
                            <TableCell>{apartment.name}</TableCell>
                            <TableCell>{apartment.address}</TableCell>
                            <TableCell>{apartment.bedrooms}</TableCell>
                            <TableCell>{apartment.bathrooms}</TableCell>
                            <TableCell>{apartment.amenities.join(', ')}</TableCell>
                            <TableCell>${apartment.rent}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>

            {/* Carousel */}
            <div className="mt-8 mx-auto">
                <Slider {...sliderSettings}>
                    {apartments.map((apartment, index) => (
                        <div key={index}>
                            <img src={apartment.image} alt={`Apartment ${index + 1}`} className="w-full h-64 object-cover" />
                        </div>
                    ))}
                </Slider>
            </div>

            {/* Email Form */}
            <div className="mt-8">
                <h2 className="text-xl font-semibold mb-2 text-center">Inquire about available units</h2>
                <div className="mb-2 mx-auto max-w-md">
                    <Text className="font-semibold">I am interested in one of the units:</Text>
                    <input
                        type="text"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder="Type your message here..."
                        className="w-full p-2 border border-gray-300 rounded"
                    />
                </div>
                <div className="mb-2 mx-auto max-w-md">
                    <Text className="font-semibold">Your Email:</Text>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Enter your email address"
                        className="w-full p-2 border border-gray-300 rounded"
                    />
                </div>
                <div className="mt-8 mb-10 text-center">
                    <Button onClick={handleSendEmail}>Send Email</Button>
                </div>
            </div>
        </div>
    );
}

export default UserDashboard;
