console.log("poop")
var movableDiv = document.getElementById("movable-div");
var picColumn = document.getElementById("picture-column");
var detailsColumn = document.getElementById("details-column");

// Create a condition that targets viewports at least 768px wide
const mediaQuery = window.matchMedia('(min-width: 753px)')

function handleTabletChange(e) {
  // Check if the media query is true
  if (e.matches) {
    // Then 
    
  }
}

// Register event listener
mediaQuery.addListener(handleTabletChange)

// Initial check
handleTabletChange(mediaQuery)