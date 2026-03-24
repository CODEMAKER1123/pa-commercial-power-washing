import os

HEADER = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PA Commercial Power Washing</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        brand: {{ blue: '#0B2341', light: '#E2E8F0', yellow: '#F59E0B', hover: '#D97706' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="font-sans text-gray-800 antialiased bg-gray-50 flex flex-col min-h-screen">

    <!-- Navigation -->
    <nav class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <a href="index.html" class="text-2xl font-extrabold text-brand-blue tracking-tight hover:opacity-80 transition">
                        PA <span class="text-blue-600">Commercial</span>
                    </a>
                </div>
                <div class="hidden md:flex items-center space-x-6">
                    <a href="about-us.html" class="text-gray-600 hover:text-brand-blue font-medium">About Us</a>
                    <div class="relative group">
                        <button class="text-gray-600 hover:text-brand-blue font-medium flex items-center">
                            Commercial Services <i class="fa-solid fa-chevron-down ml-1 text-xs"></i>
                        </button>
                        <div class="absolute left-0 mt-2 w-72 bg-white rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition duration-200 border border-gray-100 overflow-hidden">
                            <a href="facade-washing.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue border-b border-gray-50">Building & Facade Soft Washing</a>
                            <a href="parking-garages.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue border-b border-gray-50">Parking Garages & Concrete</a>
                            <a href="multi-family-hoa.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue border-b border-gray-50">Multi-Family & HOAs</a>
                            <a href="fleet-washing.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue border-b border-gray-50">Fleet Washing</a>
                            <a href="drone-lift-cleaning.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue border-b border-gray-50">Drone & High-Reach Lift Cleaning</a>
                            <a href="24-7-service.html" class="block px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand-blue">24/7 Off-Hours & Emergency</a>
                        </div>
                    </div>
                    <a href="residential.html" class="text-gray-600 hover:text-brand-blue font-medium">Residential</a>
                    <a href="mailto:mark@pacommercialpowerwashing.com" class="text-gray-600 hover:text-brand-blue font-medium">
                        <i class="fa-solid fa-envelope mr-1"></i> mark@pacommercialpowerwashing.com
                    </a>
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-2.5 px-5 rounded-md transition duration-300 shadow-md">
                        Get a Quote
                    </a>
                </div>
            </div>
        </div>
    </nav>
    <main class="flex-grow">
"""

FOOTER = """
    </main>
    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-4 gap-8 text-center md:text-left">
            <div class="col-span-1 md:col-span-1">
                <span class="text-xl font-bold text-white tracking-tight block mb-2">
                    PA Commercial
                </span>
                <span class="text-sm block mb-4">A Specialized Commercial Division of Rolling Suds</span>
                <a href="mailto:mark@pacommercialpowerwashing.com" class="text-brand-yellow hover:text-white transition"><i class="fa-solid fa-envelope mr-2"></i>mark@pacommercialpowerwashing.com</a>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-4 uppercase tracking-wider text-sm">Company</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="about-us.html" class="hover:text-white transition">About Us</a></li>
                    <li><a href="residential.html" class="hover:text-white transition">Residential Services</a></li>
                    <li><a href="index.html#quote" class="hover:text-white transition">Request Quote</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-4 uppercase tracking-wider text-sm">Commercial Services</h4>
                <ul class="space-y-2 text-sm">
                    <li><a href="facade-washing.html" class="hover:text-white transition">Facade Soft Washing</a></li>
                    <li><a href="parking-garages.html" class="hover:text-white transition">Parking Garages & Concrete</a></li>
                    <li><a href="multi-family-hoa.html" class="hover:text-white transition">Multi-Family & HOAs</a></li>
                    <li><a href="fleet-washing.html" class="hover:text-white transition">Fleet Washing</a></li>
                    <li><a href="drone-lift-cleaning.html" class="hover:text-white transition">Drone & Lift Cleaning</a></li>
                    <li><a href="24-7-service.html" class="hover:text-white transition">24/7 & Emergency Service</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold mb-4 uppercase tracking-wider text-sm">Compliance & Safety</h4>
                <ul class="space-y-2 text-sm">
                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i> OSHA Compliant</li>
                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i> Fully Insured & Bonded</li>
                    <li><i class="fa-solid fa-check text-green-500 mr-2"></i> EPA Water Reclamation</li>
                </ul>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-12 pt-8 border-t border-gray-800 text-sm text-center">
            &copy; <script>document.write(new Date().getFullYear())</script> PA Commercial Power Washing. All rights reserved.
        </div>
    </footer>
</body>
</html>
"""

INDEX_CONTENT = """
    <!-- Hero Section -->
    <section class="relative bg-brand-blue text-white overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[url('https://images.unsplash.com/photo-1541888086225-ee9b4561e1b1?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')] bg-cover bg-center"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32 flex flex-col items-center text-center">
            <span class="text-blue-300 font-semibold tracking-wider uppercase text-sm mb-4">A Division of Rolling Suds</span>
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 leading-tight max-w-4xl">
                Pennsylvania's Trusted Partner for <span class="text-brand-yellow">Large-Scale</span> Commercial Power Washing
            </h1>
            <p class="mt-4 text-lg md:text-xl text-blue-100 max-w-3xl mb-10 leading-relaxed">
                Fully insured, OSHA-compliant exterior cleaning for property managers, HOAs, and industrial facilities across PA. We work off-hours so your business never stops.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 mb-12">
                <a href="#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold text-lg py-4 px-10 rounded-md transition duration-300 shadow-lg">
                    Request a Fast Commercial Quote
                </a>
                <a href="24-7-service.html" class="bg-transparent border-2 border-white hover:bg-white hover:text-brand-blue text-white font-bold text-lg py-4 px-10 rounded-md transition duration-300">
                    24/7 Emergency Dispatch
                </a>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center max-w-4xl w-full border-t border-blue-800 pt-8 mt-4">
                <div class="flex flex-col items-center">
                    <i class="fa-solid fa-shield-halved text-3xl text-blue-400 mb-3"></i>
                    <span class="text-sm font-semibold uppercase tracking-wider text-blue-200">Fully Insured</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fa-solid fa-hard-hat text-3xl text-blue-400 mb-3"></i>
                    <span class="text-sm font-semibold uppercase tracking-wider text-blue-200">OSHA Compliant</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fa-solid fa-truck-fast text-3xl text-blue-400 mb-3"></i>
                    <span class="text-sm font-semibold uppercase tracking-wider text-blue-200">Largest Fleet in PA</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fa-solid fa-clock text-3xl text-blue-400 mb-3"></i>
                    <span class="text-sm font-semibold uppercase tracking-wider text-blue-200">24/7 Service</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Grid -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-extrabold text-brand-blue sm:text-4xl">Specialized Commercial Services</h2>
                <div class="mt-2 w-24 h-1 bg-brand-yellow mx-auto"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Facade -->
                <a href="facade-washing.html" class="block bg-gray-50 rounded-xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:border-blue-200 transition duration-300 group">
                    <div class="w-14 h-14 bg-blue-100 rounded-lg flex items-center justify-center mb-6 group-hover:bg-brand-blue transition">
                        <i class="fa-solid fa-building text-2xl text-blue-600 group-hover:text-white transition"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-blue transition">Building & Facade Soft Washing</h3>
                    <p class="text-gray-600 leading-relaxed mb-4 text-sm">Removing algae and industrial pollution without damaging masonry, stucco, or siding.</p>
                </a>

                <!-- Concrete -->
                <a href="parking-garages.html" class="block bg-gray-50 rounded-xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:border-blue-200 transition duration-300 group">
                    <div class="w-14 h-14 bg-blue-100 rounded-lg flex items-center justify-center mb-6 group-hover:bg-brand-blue transition">
                        <i class="fa-solid fa-square-parking text-2xl text-blue-600 group-hover:text-white transition"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-blue transition">Parking Garages & Concrete</h3>
                    <p class="text-gray-600 leading-relaxed mb-4 text-sm">High-traffic surface cleaning utilizing hot water extraction to remove oil and grease.</p>
                </a>

                <!-- HOA -->
                <a href="multi-family-hoa.html" class="block bg-gray-50 rounded-xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:border-blue-200 transition duration-300 group">
                    <div class="w-14 h-14 bg-blue-100 rounded-lg flex items-center justify-center mb-6 group-hover:bg-brand-blue transition">
                        <i class="fa-solid fa-house-chimney-window text-2xl text-blue-600 group-hover:text-white transition"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-blue transition">Multi-Family & HOAs</h3>
                    <p class="text-gray-600 leading-relaxed mb-4 text-sm">Standardized exterior cleaning for large residential complexes and associations.</p>
                </a>

                <!-- Fleet -->
                <a href="fleet-washing.html" class="block bg-gray-50 rounded-xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:border-blue-200 transition duration-300 group">
                    <div class="w-14 h-14 bg-blue-100 rounded-lg flex items-center justify-center mb-6 group-hover:bg-brand-blue transition">
                        <i class="fa-solid fa-truck text-2xl text-blue-600 group-hover:text-white transition"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-blue transition">Fleet Washing</h3>
                    <p class="text-gray-600 leading-relaxed mb-4 text-sm">Routine mobile washing maintenance for logistics and delivery fleets.</p>
                </a>

                <!-- Drone & Lift -->
                <a href="drone-lift-cleaning.html" class="block bg-gray-50 rounded-xl p-8 border border-gray-100 shadow-sm hover:shadow-xl hover:border-blue-200 transition duration-300 group">
                    <div class="w-14 h-14 bg-blue-100 rounded-lg flex items-center justify-center mb-6 group-hover:bg-brand-blue transition">
                        <i class="fa-solid fa-helicopter text-2xl text-blue-600 group-hover:text-white transition"></i>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-blue transition">Drone & High-Reach Lifts</h3>
                    <p class="text-gray-600 leading-relaxed mb-4 text-sm">Mid and high-rise cleaning without scaffolding. Boom lifts and drone soft-washing.</p>
                </a>

                <!-- 24/7 -->
                <a href="24-7-service.html" class="block bg-brand-blue rounded-xl p-8 border border-blue-800 shadow-lg hover:shadow-xl transition duration-300 group">
                    <div class="w-14 h-14 bg-brand-yellow rounded-lg flex items-center justify-center mb-6">
                        <i class="fa-solid fa-clock text-2xl text-white"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3">24/7 Off-Hours & Emergency</h3>
                    <p class="text-blue-100 leading-relaxed mb-4 text-sm">Spill response, graffiti removal, and overnight service so your business never stops.</p>
                </a>
            </div>
        </div>
    </section>

    <!-- Why Property Managers Choose Us -->
    <section class="py-20 bg-gray-50 border-y border-gray-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-extrabold text-brand-blue sm:text-4xl">Why Property Managers Choose Us</h2>
                <div class="mt-2 w-24 h-1 bg-brand-yellow mx-auto"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
                <div class="p-6">
                    <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
                        <i class="fa-solid fa-stopwatch text-3xl text-brand-yellow"></i>
                    </div>
                    <h3 class="text-xl font-bold text-brand-blue mb-4">Massive Scale & Speed</h3>
                    <p class="text-gray-600">We deploy multiple state-of-the-art rigs simultaneously. We finish 100,000+ sq ft facilities in days, not weeks, drastically reducing on-site time.</p>
                </div>
                <div class="p-6">
                    <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
                        <i class="fa-solid fa-moon text-3xl text-brand-yellow"></i>
                    </div>
                    <h3 class="text-xl font-bold text-brand-blue mb-4">Zero Operational Disruption</h3>
                    <p class="text-gray-600">Your tenants and customers come first. We schedule around your operations, including night and weekend shifts, so your business is never inconvenienced.</p>
                </div>
                <div class="p-6">
                    <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm border border-gray-100">
                        <i class="fa-solid fa-file-contract text-3xl text-brand-yellow"></i>
                    </div>
                    <h3 class="text-xl font-bold text-brand-blue mb-4">Bulletproof Compliance</h3>
                    <p class="text-gray-600">We carry comprehensive liability insurance and workers' comp. Our strict environmental compliance and water reclamation protocols protect you from EPA fines.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Lead Capture Form -->
    <section id="quote" class="py-24 bg-brand-blue">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="bg-white rounded-2xl shadow-2xl overflow-hidden">
                <div class="p-10 md:p-14">
                    <h2 class="text-3xl font-extrabold text-brand-blue text-center mb-2">Get Your Facility Cleaned.</h2>
                    <p class="text-gray-500 text-center mb-8 text-lg">Zero Headaches. Fast Proposals.</p>
                    
                    <form action="mailto:mark@pacommercialpowerwashing.com" method="POST" enctype="text/plain" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                                <input type="text" name="name" required class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Company / Organization</label>
                                <input type="text" name="company" required class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition">
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Work Email</label>
                                <input type="email" name="email" required class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Direct Phone</label>
                                <input type="tel" name="phone" required class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition">
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Property Type</label>
                            <select name="property_type" required class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition bg-white">
                                <option value="" disabled selected>Select facility type...</option>
                                <option value="HOA / Multi-Family">HOA / Multi-Family</option>
                                <option value="Retail / Strip Mall">Retail / Strip Mall</option>
                                <option value="Industrial / Warehouse">Industrial / Warehouse</option>
                                <option value="Office Building">Office Building</option>
                                <option value="Parking Garage">Parking Garage</option>
                                <option value="Fleet Vehicles">Fleet Vehicles</option>
                                <option value="Residential Home">Residential Home</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Project Details</label>
                            <textarea name="details" rows="4" class="w-full px-4 py-3 border border-gray-300 rounded-md focus:ring-brand-yellow focus:border-brand-yellow outline-none transition"></textarea>
                        </div>

                        <button type="submit" class="w-full bg-brand-yellow hover:bg-brand-hover text-white font-bold text-lg py-4 px-8 rounded-md transition duration-300 shadow-lg">
                            Get Your Custom Proposal
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

PAGES = {
    "index.html": {
        "title": "Trusted Partner for Large-Scale Facilities",
        "description": "Fully insured, OSHA-compliant exterior cleaning for property managers, HOAs, and industrial facilities across Pennsylvania.",
        "content": INDEX_CONTENT
    },
    "about-us.html": {
        "title": "About Us",
        "description": "Backed by the largest power washing franchise network in the US, PA Commercial Power Washing brings unmatched scale, safety, and speed to PA.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">About PA Commercial Power Washing</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Unmatched scale, uncompromised safety, and localized expertise.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <h2 class="text-3xl font-bold text-brand-blue mb-6">Built for the Toughest Commercial Jobs</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">PA Commercial Power Washing is a specialized division of the Rolling Suds franchise network—the largest power washing operation in the United States. We created this division specifically to address the unique logistical, compliance, and insurance needs of Pennsylvania's largest facilities, property managers, and HOAs.</p>
                <h2 class="text-2xl font-bold text-brand-blue mb-4">Why Commercial Clients Trust Us</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Most local power washers are "guy-in-a-truck" operations. They lack the equipment to finish a 100,000 sq ft facility quickly, and more importantly, they lack the multi-million dollar liability insurance and workers' compensation required to legally operate on your property.</p>
                <ul class="space-y-4 text-gray-700">
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Massive Fleet:</strong> We can deploy multiple high-output rigs simultaneously to cut job times by 70%.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Strict Safety & OSHA Compliance:</strong> Every technician undergoes rigorous, documented safety training.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Full Insurance & Bonding:</strong> We carry extensive commercial liability and workers' comp policies, protecting your organization from risk.</li>
                </ul>
            </div>
            <div>
                <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Commercial Operations" class="rounded-xl shadow-2xl">
            </div>
        </div>
    </div>
        """
    },
    "drone-lift-cleaning.html": {
        "title": "Drone & Boom Lift High-Reach Cleaning",
        "description": "High-rise facade and window cleaning using advanced boom lifts and commercial drone soft-washing technology in PA.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Drone & High-Reach Lift Cleaning</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Reaching the unreachable. Safe, cost-effective cleaning for mid and high-rise structures.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1">
                <img src="https://images.unsplash.com/photo-1508450859948-4e04fabaa4ea?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="High Reach Boom Lift" class="rounded-xl shadow-2xl">
            </div>
            <div class="order-1 lg:order-2">
                <h2 class="text-3xl font-bold text-brand-blue mb-6">No Scaffolding? No Problem.</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">For mid-rise and high-rise facilities, traditional scaffolding or swing-stages are incredibly expensive, slow to deploy, and highly disruptive to your building's occupants. We offer a modern alternative.</p>
                <h2 class="text-2xl font-bold text-brand-blue mb-4">Advanced Boom Lifts & Drone Soft-Washing</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Our crews are fully certified in aerial lift operation. For buildings up to 10 stories, our commercial boom lifts allow us to safely apply our soft-wash detergents and high-pressure rinses precisely where needed. For structures even higher, or those with difficult terrain access, we utilize industrial drone washing technology to clean your facade without ever putting a worker at dangerous heights.</p>
                <ul class="space-y-4 text-gray-700">
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Massive Cost Savings:</strong> Eliminate the thousands of dollars typically spent on scaffolding erection.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Unmatched Safety:</strong> Drastically reduces liability and fall risks on your property.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Rapid Deployment:</strong> We arrive, clean, and demobilize in a fraction of the time.</li>
                </ul>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Request a High-Reach Estimate</a>
                </div>
            </div>
        </div>
    </div>
        """
    },
    "24-7-service.html": {
        "title": "24/7 Off-Hours & Emergency Power Washing",
        "description": "Emergency spill response, graffiti removal, and overnight power washing services so your business never stops.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">24/7 Off-Hours & Emergency Service</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Your business never stops. Neither do we.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <h2 class="text-3xl font-bold text-brand-blue mb-6">Zero Operational Disruption</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Retail centers, drive-thrus, and busy logistics hubs cannot afford to shut down during the day. Water hoses and cleaning crews in the middle of business hours annoy customers and create massive safety hazards.</p>
                <h2 class="text-2xl font-bold text-brand-blue mb-4">Night Shifts & Rapid Emergency Response</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">We schedule our largest commercial cleanings at 2:00 AM, working entirely under the radar so your property is pristine by the time the first customer arrives. Furthermore, when accidents happen, we respond rapidly.</p>
                <ul class="space-y-4 text-gray-700">
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Emergency Spill Response:</strong> Rapid hot-water extraction for hydraulic fluid, grease drops, and chemical spills in loading docks or parking lots.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Graffiti Removal:</strong> Vandalism damages your brand. We rapidly deploy specialized chemical treatments to dissolve paint from masonry without ghosting.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Self-Contained Rigs:</strong> Our night-shift trucks carry their own water and whisper-quiet generators. We don't need access to your building's utilities.</li>
                </ul>
                <div class="mt-10 flex gap-4">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Schedule Off-Hours Wash</a>
                </div>
            </div>
            <div>
                <img src="https://images.unsplash.com/photo-1542038784456-1ea8e935640e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Nighttime Operations" class="rounded-xl shadow-2xl">
            </div>
        </div>
    </div>
        """
    },
    "residential.html": {
        "title": "Residential Power Washing in PA",
        "description": "Commercial-grade power washing and soft washing services for Pennsylvania homeowners.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Residential Power Washing</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Commercial-grade equipment and expertise, delivered straight to your driveway.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1">
                <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Beautiful Residential Home" class="rounded-xl shadow-2xl">
            </div>
            <div class="order-1 lg:order-2">
                <h2 class="text-3xl font-bold text-brand-blue mb-6">Yes, We Do Homes.</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">While our commercial fleet handles millions of square feet of industrial space, we bring that exact same commercial-grade equipment, 200°F hot water extraction, and rigorous training to Pennsylvania homeowners.</p>
                <h2 class="text-2xl font-bold text-brand-blue mb-4">Complete Home Exterior Care</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Your home is your largest investment. Don't trust it to a guy with a rental pressure washer who might blast the paint off your deck or force water behind your vinyl siding. We use specialized soft washing techniques to gently clean your home's exterior.</p>
                <ul class="space-y-4 text-gray-700">
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>House Soft Washing:</strong> Safe removal of algae and mold from siding, brick, and stucco without damaging high pressure.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Driveways & Patios:</strong> Deep cleaning concrete, pavers, and stamped concrete using surface cleaners.</li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-brand-yellow mt-1 mr-3"></i> <strong>Roof Cleaning:</strong> Eliminating black streaks (Gloeocapsa Magma) safely to extend the life of your shingles.</li>
                </ul>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Get a Free Home Quote</a>
                </div>
            </div>
        </div>
    </div>
        """
    },
    "facade-washing.html": {
        "title": "Commercial Building & Facade Soft Washing",
        "description": "Professional exterior facade cleaning for commercial buildings in PA.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Building & Facade Soft Washing</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Protect your asset value and eliminate organic growth without risking damage to masonry, stucco, or siding.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <h2 class="text-3xl font-bold text-brand-blue mb-6">The Problem with Traditional Pressure Washing</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Most power washing companies rely entirely on high pressure. When applied to delicate commercial facades like brick, Dryvit, stucco, or older masonry, high pressure can strip away protective coatings, blow out mortar joints, and drive water deep into the building envelope.</p>
                <h2 class="text-2xl font-bold text-brand-blue mb-4">Our Soft Washing Solution</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Rolling Suds utilizes proprietary soft washing technology for building facades. We apply specially formulated, environmentally friendly detergents at low pressure to kill algae, mildew, and lichen at the root.</p>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Request a Quote for Your Building</a>
                </div>
            </div>
            <div>
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Commercial Building Facade" class="rounded-xl shadow-2xl">
            </div>
        </div>
    </div>
        """
    },
    "parking-garages.html": {
        "title": "Commercial Parking Garage & Concrete Cleaning",
        "description": "High-traffic surface cleaning utilizing hot water extraction for parking garages.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Parking Garages & Concrete Cleaning</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Mitigate slip-and-fall liabilities and restore high-traffic surfaces with industrial hot water extraction.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1">
                <img src="https://images.unsplash.com/photo-1573348722427-f1d6819fdf98?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Commercial Parking Garage" class="rounded-xl shadow-2xl">
            </div>
            <div class="order-1 lg:order-2">
                <h2 class="text-3xl font-bold text-brand-blue mb-6">High-Traffic Surfaces Demand Heavy-Duty Solutions</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Parking garages, loading docks, and drive-thrus take a massive beating. Layered oil drips, transmission fluid, chewing gum, and tire marks aren't just ugly—they create significant slip-and-fall liability.</p>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Get a Concrete Cleaning Proposal</a>
                </div>
            </div>
        </div>
    </div>
        """
    },
    "multi-family-hoa.html": {
        "title": "HOA & Multi-Family Property Power Washing",
        "description": "Standardized exterior cleaning for large residential complexes.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Multi-Family & HOA Exterior Cleaning</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Uniform results at massive scale. We coordinate directly with property managers.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
                <h2 class="text-3xl font-bold text-brand-blue mb-6">The Logistics of Scale</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">Cleaning a 300-unit condominium complex is a logistics challenge. Property managers need a vendor who can deliver uniform results across dozens of buildings without generating complaints from residents.</p>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Request an HOA Site Walk</a>
                </div>
            </div>
            <div>
                <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Multi Family Property" class="rounded-xl shadow-2xl">
            </div>
        </div>
    </div>
        """
    },
    "fleet-washing.html": {
        "title": "Commercial Fleet Washing",
        "description": "Routine washing and maintenance for logistics and delivery fleets.",
        "content": """
    <div class="bg-brand-blue py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl font-extrabold text-white sm:text-5xl mb-4">Commercial Fleet Washing</h1>
            <p class="text-xl text-blue-200 max-w-3xl mx-auto">Keep your rolling billboards pristine and protect vehicle undercarriages.</p>
        </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="order-2 lg:order-1">
                <img src="https://images.unsplash.com/photo-1586528116311-ad8ed7c8084f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Commercial Delivery Trucks" class="rounded-xl shadow-2xl">
            </div>
            <div class="order-1 lg:order-2">
                <h2 class="text-3xl font-bold text-brand-blue mb-6">Your Fleet is Your Brand</h2>
                <p class="text-gray-600 mb-6 leading-relaxed">When a dirty delivery truck pulls up to a customer's location, it damages your brand reputation. Beyond aesthetics, winter road salts and industrial grime actively corrode your vehicles.</p>
                <div class="mt-10">
                    <a href="index.html#quote" class="bg-brand-yellow hover:bg-brand-hover text-white font-bold py-3 px-8 rounded-md transition duration-300 shadow-md inline-block">Schedule a Fleet Wash Demo</a>
                </div>
            </div>
        </div>
    </div>
        """
    }
}

for filename, data in PAGES.items():
    full_html = HEADER.format(title=data["title"], description=data["description"]) + data["content"] + FOOTER
    with open(filename, 'w') as f:
        f.write(full_html)
    print(f"Generated {filename}")
