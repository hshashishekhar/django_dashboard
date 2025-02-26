// Initialize Lucide icons
lucide.createIcons();

// Theme toggle functionality
const themeToggle = document.getElementById('themeToggle');

// Check for saved theme preference or default to light
if (localStorage.getItem('theme') === 'dark' || 
    (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
}

// Toggle theme
themeToggle.addEventListener('click', () => {
    if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
});

// Profile dropdown functionality
const profileButton = document.getElementById('profileButton');
const profileDropdown = document.getElementById('profileDropdown');

profileButton.addEventListener('click', (e) => {
    e.stopPropagation();
    profileDropdown.classList.toggle('hidden');
});

document.addEventListener('click', (e) => {
    if (!profileButton.contains(e.target)) {
        profileDropdown.classList.add('hidden');
    }
});
// Select the hamburger menu button and the sidebar
// Select elements
const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');

// Helper function to check if the screen is large
function isLargeScreen() {
    return window.matchMedia('(min-width: 1024px)').matches;
}

// Function to toggle the sidebar and adjust the content margin
function toggleSidebar() {
    // Toggle the sidebar visibility
    sidebar.classList.toggle('hidden');

    // Adjust the content margin based on screen size
    if (!isLargeScreen()) {
        content.classList.toggle('ml-0');
        console.log("here");
        content.classList.toggle('ml-1'); // Match the sidebar width
    }
}

// Add a click event listener to toggle the sidebar
menuToggle.addEventListener('click', () => {
    toggleSidebar();
});

if (isLargeScreen()) {
    menuToggle.style.display = 'none'; // Hide the hamburger menu on large screens
} else {
    menuToggle.style.display = 'block'; // Show the hamburger menu on small screens
}

// Add this to your existing JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const crmButton = document.getElementById('crmButton');
    const crmDropdown = document.getElementById('crmDropdown');

    // Toggle dropdown on chevron click
    crmButton.querySelector('[data-lucide="chevron-down"]').addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        crmDropdown.classList.toggle('hidden');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
        if (!crmButton.contains(e.target) && !crmDropdown.contains(e.target)) {
            crmDropdown.classList.add('hidden');
        }
    });
});