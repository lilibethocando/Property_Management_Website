import main_picture from '../assets/chicago.jpeg';

const TopSection = () => {
    return (
        <div className="relative bg-cover bg-center bg-no-repeat h-96" style={{ backgroundImage: `url(${main_picture})` }}>
            <div className="absolute inset-0 bg-black bg-opacity-50"></div>
            <div className="container mx-auto relative h-full flex items-center justify-center">
                <div className="text-center text-white">
                    <h1 className="text-4xl font-bold mb-6">Smart Property Management</h1>
                    <p className="text-lg mb-8">Simplify property management with ease and efficiency</p>
                    {/* <a href="#!" className="bg-gradient-to-r from-green-400 to-green-200 py-2 px-6 rounded-md">Get Started</a> */}
                </div>
            </div>
        </div>
    )
}

export default TopSection;