import React from 'react'
import Navbar from '../components/Navbar'
import TopSection from '../components/TopSection'
import SignUp from '../components/SignUp'
import FeatureSection from '../components/FeatureSection'
import Footer from '../components/Footer'

const LandingPage = () => {
    return (
        <>
        <div className="max-w-6xl mx-auto pt-20 px-6">
            <TopSection />
            <FeatureSection />
            <Footer />
            </div>
        </>
    )
};

export default LandingPage;