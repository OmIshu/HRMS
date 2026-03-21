# HRMS UI - Design System & Customization Guide

## Color Scheme

### Primary Colors
```
Gradient Primary: #667eea → #764ba2
Usage: Buttons, sidebar highlights, card borders, focus states
```

### Status Colors
```
✓ Success/Present: #10b981 (Green)
✕ Danger/Absent: #dc2626 (Red)
⚠ Warning: #f59e0b (Orange)
ℹ Info: #667eea (Blue)
```

### Neutral Colors
```
Background: #f7fafc (Very light blue-gray)
Surface: #ffffff (White)
Border: #e2e8f0 (Light gray)
Text Primary: #1a202c (Dark blue-gray)
Text Secondary: #718096 (Medium gray)
Text Muted: #a0aec0 (Light gray)
```

### Interactive Elements
```
Sidebar Background: #1a202c → #2d3748 (Dark gradient)
Sidebar Text: #cbd5e0 (Light gray)
Sidebar Active: rgba(102, 126, 234, 0.15) (Light purple background)
```

## Typography

### Font Family
```
Primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto
```

### Font Sizes & Weights
```
h1: 2.5rem, weight 700 (Dashboard title)
h2: 1.8rem, weight 700 (Page sections)
h3: 1.3rem, weight 700 (Card headers)
h4: 1.1rem, weight 700 (Subsections)
h5: 0.9rem, weight 700 (Small headers)
Body: 0.95rem, weight 400
Label: 0.95rem, weight 600
Small: 0.8rem, weight 400
Tiny: 0.75rem, weight 500
```

## Button Styles

### Primary Button
```css
.btn-primary {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
  font-weight: 600;
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
}
```

### Success Button
```css
.btn-success {
  background: linear-gradient(135deg, #34d399, #10b981);
  color: white;
  padding: 12px 20px;
  border-radius: 6px;
  font-weight: 600;
}
```

### Danger Button
```css
.btn-danger {
  background-color: #f87171;
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
  font-weight: 600;
}
.btn-danger:hover {
  background-color: #dc2626;
}
```

## Form Elements

### Input Focus State
```css
border-color: #667eea;
box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
```

### Input Error State
```css
border-color: #dc2626;
background-color: #fee2e2;
box-shadow: 0 0 0 4px rgba(220, 38, 38, 0.1);
```

## Card Styling

### Basic Card
```css
background: white;
border: 1px solid #e2e8f0;
border-radius: 12px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
padding: 24px;
transition: box-shadow 0.3s ease;
```

### Card Hover State
```css
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
```

### Card Header
```css
background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
border-bottom: 1px solid #e2e8f0;
padding: 24px;
```

## Spacing System

```
xs: 4px
sm: 8px
md: 12px
lg: 16px
xl: 20px
2xl: 24px
3xl: 32px
```

## Component-Specific Customizations

### Sidebar
Primary Files: `src/components/Sidebar.js`, `src/components/Sidebar.css`

To change sidebar width:
```css
.sidebar {
  width: 260px; /* Change this value */
}

.main-wrapper {
  margin-left: 260px; /* Must match sidebar width */
}
```

To change sidebar colors:
```css
.sidebar {
  background: linear-gradient(180deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
}
```

### Dashboard Cards
Primary Files: `src/components/Dashboard.js`, `src/components/Dashboard.css`

Card icons have different gradients:
```css
.stat-icon.total-employees {
  background: linear-gradient(135deg, #667eea, #764ba2); /* Purple */
}

.stat-icon.total-departments {
  background: linear-gradient(135deg, #a78bfa, #7c3aed); /* Purple */
}

.stat-icon.present-today {
  background: linear-gradient(135deg, #34d399, #10b981); /* Green */
}

.stat-icon.absent-today {
  background: linear-gradient(135deg, #f87171, #dc2626); /* Red */
}
```

### Tables
Primary Files: Component CSS files

Table header gradient:
```css
.attendance-table thead {
  background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
}
```

## Responsive Breakpoints

```
Mobile Small: < 480px
Mobile Large: 480px - 768px
Tablet: 768px - 1024px
Desktop: 1024px - 1400px
Desktop Large: > 1400px
```

### Layout Changes by Breakpoint
- **< 768px**: Single column grids, full-width forms
- **768px - 1024px**: Adjusted spacing, optimized layouts
- **> 1024px**: Full sidebar visible, multi-column grids

## Animation & Transitions

### Standard Timing
```css
transition: all 0.3s ease;
```

### Specific Animations
```css
/* Card lift on hover */
transform: translateY(-4px);

/* Button press effect */
transform: translateY(-2px);

/* Loading spinner */
animation: spin 1s linear infinite;

/* Fade in */
animation: slideIn 0.3s ease;
```

## Shadows

### Subtle Shadow
```css
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
```

### Medium Shadow
```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
```

### Large Shadow
```css
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
```

## Status Badges

### Present Status
```css
background-color: #d1fae5;
color: #065f46;
```

### Absent Status
```css
background-color: #fee2e2;
color: #991b1b;
```

## Customization Examples

### Change Primary Color Throughout
Search for `#667eea` and `#764ba2` and replace with your colors:
```
#667eea → Your Primary Color
#764ba2 → Your Secondary Color
```

### Modify Sidebar Width
1. Change `.sidebar { width: 260px; }` in Sidebar.css
2. Change `.main-wrapper { margin-left: 260px; }` in App.css

### Adjust Border Radius
Current standard: `border-radius: 8-12px;`
Customize all occurrences for a more rounded/square look

### Change Text Colors
Primary text: `#1a202c`
Secondary text: `#718096`
Muted text: `#a0aec0`

## Dark Mode Implementation (Future)

When implementing dark mode, create a CSS variable system:
```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f7fafc;
  --text-primary: #1a202c;
  --text-secondary: #718096;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-primary: #1a202c;
    --bg-secondary: #2d3748;
    --text-primary: #f7fafc;
    --text-secondary: #cbd5e0;
  }
}
```

## Accessibility Features

- Focus states clearly visible
- Color contrast ratios meet WCAG AA standards
- Semantic HTML structure
- ARIA labels where needed
- Keyboard navigation support
- Reduced motion support ready

## Performance Tips

1. CSS transitions instead of animations
2. GPU-accelerated transforms (translate, rotate)
3. Minimal box-shadow usage
4. Efficient gradient usage
5. SVG icons for scalability
6. Optimized image sizes

---

For questions or customizations, refer to the specific component files and their CSS modules.
