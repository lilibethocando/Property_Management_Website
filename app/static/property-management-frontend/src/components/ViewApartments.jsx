import React from 'react';
import { Card, Button, Container, Row, Col } from 'react-bootstrap'; 
import { Link } from 'react-router-dom';

import apt1 from '../assets/apt1.jpeg';
import apt2 from '../assets/apt2.webp';
import apt3 from '../assets/apt3.jpeg';
import apt4 from '../assets/apt4.jpeg';
import apt5 from '../assets/apt5.jpeg';
import apt6 from '../assets/apt6.jpeg';
import apt7 from '../assets/apt7.jpeg';
import apt8 from '../assets/apt8.jpeg';
import apt9 from '../assets/apt9.jpeg';
import apt10 from '../assets/apt10.jpeg';
import apt11 from '../assets/apt11.jpeg';
import apt12 from '../assets/apt12.jpeg';

const ViewApartment = () => {
    // Fake data for apartments
    const apartments = [
        {
            name: 'Apartment 1',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 1,
            amenities: ['Swimming Pool', 'Gym', 'Parking'],
            rent: 1500,
            image: apt1 
        },
        {
            name: 'Apartment 2',
            address: 'Chicago, IL',
            bedrooms: 3,
            bathrooms: 2,
            amenities: ['Fitness Center', 'Balcony', 'Laundry'],
            rent: 2000,
            image: apt2 
        },
        {
            name: 'Apartment 3',
            address: 'Chicago, IL',
            bedrooms: 1,
            bathrooms: 1,
            amenities: ['Roof Deck', 'Dishwasher', 'Pet Friendly'],
            rent: 1200,
            image: apt11 
        },
        {
            name: 'Apartment 4',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 2,
            amenities: ['Pool', 'Dishwasher', 'Garden', 'Parking','Roof Deck', 'Laundry'],
            rent: 1800,
            image: apt4
        },
        {
            name: 'Apartment 5',
            address: 'Chicago, IL',
            bedrooms: 3,
            bathrooms: 2,
            amenities: ['Playground', 'Garage', 'Gym'],
            rent: 2200,
            image: apt5 
        },
        {
            name: 'Apartment 6',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 1,
            amenities: ['Balcony', 'Fitness Center', 'Dishwasher'],
            rent: 1600,
            image: apt6 
        },
        {
            name: 'Apartment 7',
            address: 'Chicago, IL',
            bedrooms: 1,
            bathrooms: 1,
            amenities: ['Laundry', 'Parking', 'Pet Friendly'],
            rent: 1300,
            image: apt7
        },
        {
            name: 'Apartment 8',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 2,
            amenities: ['Roof Deck', 'Swimming Pool', 'Garage'],
            rent: 1900,
            image: apt8
        },
        {
            name: 'Apartment 9',
            address: 'Chicago, IL',
            bedrooms: 3,
            bathrooms: 2,
            amenities: ['Gym', 'Dishwasher', 'Playground'],
            rent: 2300,
            image: apt9 
        },
        {
            name: 'Apartment 10',
            address: 'Chicago, IL',
            bedrooms: 2,
            bathrooms: 1,
            amenities: ['Parking', 'Balcony', 'Fitness Center'],
            rent: 1700,
            image: apt10
        },
    ];

    return (
        <Container className="mt-5">
            <h1 className="text-center mb-4" style={{ fontSize: '2rem', fontWeight: 'bold' }}>See some of our luxury units below</h1>
            <Row className="justify-content-center">
                {apartments.map((apt, index) => (
                    <Col key={index} lg={3} md={4} sm={6} className="mb-3">
                        <Card style={{ backgroundColor: 'rgba(255, 255, 255, 0.7)' }}>
                            <Card.Img variant="top" src={apt.image} />
                            <Card.Body>
                                <Card.Title>{apt.name}</Card.Title>
                                <Card.Text>
                                    <strong>Location:</strong> {apt.address}<br />
                                    <strong>Bedrooms:</strong> {apt.bedrooms}<br />
                                    <strong>Bathrooms:</strong> {apt.bathrooms}<br />
                                    <strong>Amenities:</strong> {apt.amenities.join(', ')}
                                <br />
                                <strong>Rent:</strong> ${apt.rent}/month
                            </Card.Text>
                            <Link to="/availability">
                                <Button variant="primary">Check Availability</Button>
                            </Link>
                        </Card.Body>
                    </Card>
                </Col>
            ))}
        </Row>
        <p className="text-center mb-5 mt-4">If anything interested you, check availability and get in contact with our representatives.</p>
    </Container>
);
};

export default ViewApartment;