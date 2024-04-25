

const FeatureSection = () => {
    return (
        <div className="relative mt-20 border-b border-neutral-800 min-h-[800px]">
            <div className="container mx-auto relative h-full flex flex-col items-center justify-center">
                <h2 className="text-4xl font-bold mb-6">Services</h2>
                <p className="text-lg mb-8">Streamline property management, cater to tenant requirements, and facilitate seamless transactions for all rental-related needs.</p>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Property Management</h3>
                        <p className="text-lg">Manage your properties with ease. Add, update, and delete properties.</p>
                    </div>
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Tenant Management</h3>
                        <p className="text-lg">Manage your tenants with ease. Add, update, and delete tenants.</p>
                    </div>
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Payment Management</h3>
                        <p className="text-lg">Manage payments with ease. Add, update, and delete payments.</p>
                    </div>
                </div>
            </div>
                <p className="text-lg mb-8"></p>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Property Management</h3>
                        <p className="text-lg">Manage your properties with ease. Add, update, and delete properties.</p>
                    </div>
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Tenant Management</h3>
                        <p className="text-lg">Manage your tenants with ease. Add, update, and delete tenants.</p>
                    </div>
                    <div className="bg-neutral-200 p-8 rounded-md">
                        <h3 className="text-2xl font-bold mb-4">Payment Management</h3>
                        <p className="text-lg">Manage payments with ease. Add, update, and delete payments.</p>
                    </div>
                </div>
            </div>

        
    )
}

export default FeatureSection