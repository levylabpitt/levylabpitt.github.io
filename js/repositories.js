// This script dynamically generates a list of repositories with their display names and badges.
// It uses the GitHub API to fetch the latest release information and displays it on a webpage.
// Reusable configuration with username
const config = {
  user: "levylabpitt"
};

// All repositories with their display names in categories
const repositories = {
  dataAcquisition: [
    { repo: "Multichannel-Lockin", displayName: "Multichannel Lock-In" },
    { repo: "Krohn-Hite-7008", displayName: "Krohn Hite 7008" }
  ],
  cryogenicSystems: [
    { repo: "Leiden-FP-and-TC", displayName: "LC TC and FrontPanel" },
    { repo: "Oxford-1820", displayName: "Oxford 1820 Monitor" },
    { repo: "Oxford-VRM", displayName: "Oxford VRM Monitor" },
    { repo: "Montana-Instruments-Cryostation", displayName: "Montana Instruments Cryostation" },
    { repo: "PPMS-Monitor-and-Control", displayName: "PPMS Monitor and Control" },
    { repo: "Razorbill-RP100", displayName: "Razorbill RP100 Monitor" },
    { repo: "Xeryon-Rotator", displayName: "Xeryon Rotator" }
  ],
  developmentFrameworks: [
    { repo: "Instrument-Framework", displayName: "Instrument Framework" },
    { repo: "Instrument-Framework-Template", displayName: "Instrument Framework Template" }
  ],
  dataAnalysis: [
    { repo: "Database-Viewer", displayName: "Database Viewer" },
    { repo: "Data-Analysis", displayName: "Data Analysis" },
    { repo: "Data-Analysis-Framework", displayName: "Data Analysis Framework" }
  ]
};

// Function to create a badge with consistent styling
function createBadge(url, alt, linkUrl = null) {
  const img = document.createElement('img');
  img.className = 'release-badge';
  img.src = url;
  img.alt = alt;
  img.style.height = '20px'; // Ensure consistent height
  
  // Handle errors for badges that might not exist
  img.onerror = function() {
    img.style.display = 'none';
  };
  
  // If a link URL is provided, wrap the badge in an anchor tag
  if (linkUrl) {
    const link = document.createElement('a');
    link.href = linkUrl;
    link.style.borderBottom = 'none';
    link.style.display = 'flex'; // Use flex for better alignment
    link.style.alignItems = 'center'; // Center items vertically
    link.appendChild(img);
    return link;
  }
  
  return img;
}

// Function to create a repository entry with badges
function createRepoEntry(repo, displayName) {
  const li = document.createElement('li');
  
  // Main container to hold both the link and badges
  const container = document.createElement('div');
  
  // Link to repository
  const a = document.createElement('a');
  a.href = `https://github.com/${config.user}/${repo}`;
  a.textContent = displayName || repo;
  container.appendChild(a);
  
  // Add a line break for badges to appear below
  container.appendChild(document.createElement('br'));
  
  // Badge container
  const badgeContainer = document.createElement('div');
  badgeContainer.className = 'badge-container';
  
  // ORDER CHANGE: 1. Tag badge with link to tags page
  const tagBadge = createBadge(
    `https://img.shields.io/github/v/tag/${config.user}/${repo}?style=flat-square&label=tag`,
    'Latest Tag',
    `https://github.com/${config.user}/${repo}/tags`
  );
  badgeContainer.appendChild(tagBadge);
  
  // ORDER CHANGE: 2. Release badge with link
  const releaseBadge = createBadge(
    `https://img.shields.io/github/v/release/${config.user}/${repo}?style=flat-square&label=release`,
    'release',
    `https://github.com/${config.user}/${repo}/releases/latest`
  );
  badgeContainer.appendChild(releaseBadge);
  
  // ORDER CHANGE: 3. Downloads badge
  const downloadsBadge = createBadge(
    `https://img.shields.io/github/downloads/${config.user}/${repo}/total?style=flat-square&label=downloads`,
    'Downloads'
  );
  badgeContainer.appendChild(downloadsBadge);
  
  // Add badges to container
  container.appendChild(badgeContainer);
  
  // Add container to list item
  li.appendChild(container);
  
  return li;
}

// Populate repository entries when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  // Error handling function
  function populateList(elementId, repoArray) {
    const listElement = document.getElementById(elementId);
    if (!listElement) {
      console.error(`Element with ID ${elementId} not found`);
      return;
    }
    
    // Clear any existing content
    listElement.innerHTML = '';
    
    // Add new items
    repoArray.forEach(item => {
      listElement.appendChild(createRepoEntry(item.repo, item.displayName));
    });
  }

  // Populate all category lists
  populateList('data-acquisition-list', repositories.dataAcquisition);
  populateList('cryogenic-systems-list', repositories.cryogenicSystems);
  populateList('development-frameworks-list', repositories.developmentFrameworks);
  populateList('data-analysis-list', repositories.dataAnalysis);
});