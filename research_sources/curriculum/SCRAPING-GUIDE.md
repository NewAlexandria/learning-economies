# Cybersecurity and OT Security Program Information Scraping Guide

## Purpose
This guide provides instructions for gathering curriculum information for cybersecurity and Operational Technology (OT) security training programs and adding them to the curriculum directory.

## Directory Structure
All program information should be stored in: `/Users/zak/src/projects/learning-economies/research_sources/curriculum/`

## Step-by-Step Process

### Step 1: Identify Programs to Research
- Search for cybersecurity master's programs with OT/ICS/SCADA focus
- Search for OT security training programs
- Search for industrial control systems security programs
- Search for cyber-physical systems security programs
- Look for both academic degree programs and professional training programs

**Search Terms to Use:**
- "cybersecurity master's degree" + "OT security" OR "operational technology"
- "ICS security training" OR "SCADA security training"
- "industrial control systems" + "cybersecurity" + "curriculum"
- "cyber-physical systems" + "security" + "master's"
- "OT security certification" OR "OT security training"
- Specific institutions: SANS, CERT, ISA, universities

### Step 2: Gather Program Information
For each program, collect the following information:

#### Required Information:
1. **Institution Name**
2. **Program Name**
3. **Program Type** (Academic Degree / Professional Training / Research Centre / Certificate)
4. **Format** (Online / On-Campus / Hybrid)
5. **Total Credits/Courses** (if applicable)
6. **Duration** (if applicable)
7. **Tuition/Cost** (if available)
8. **Official URL** (curriculum page preferred)

#### Curriculum Details:
- **Core Courses** (with course codes if available)
- **Required Courses** (foundation, prerequisite courses)
- **Elective Courses** (if applicable)
- **Specializations/Tracks** (if applicable)
- **Course Descriptions** (brief descriptions of key courses)
- **Prerequisites** (if applicable)

#### OT Security Relevance:
- Does the program have direct OT security focus?
- Does it have OT-relevant components?
- What specific OT topics are covered? (ICS, SCADA, critical infrastructure, IoT security, etc.)

### Step 3: Create Individual Program File
Create a markdown file for each program using the naming convention:
`[institution-name-lowercase]-[program-name-lowercase].md`

**Example:** `georgetown-university-itm-cybersecurity.md`

#### File Template:
```markdown
# [Institution Name] - [Program Name]

## Program Overview
- **Institution**: [Full institution name]
- **Program**: [Full program name]
- **Format**: [Online/On-Campus/Hybrid]
- **Total Credits/Courses**: [Number]
- **Duration**: [Time period]
- **Tuition**: [Cost if available]
- **URL**: [Official curriculum URL]

## Program Structure

[Describe the overall structure - tracks, specializations, etc.]

### Core Courses ([X credits])
1. **[Course Code]: [Course Name]**
   - [Brief description if available]

### Required/Foundation Courses ([X credits])
[List all required courses]

### Elective Courses ([X credits])
[List elective options, especially OT/cybersecurity related]

### Specializations/Tracks
[If applicable, list each track with description]

## OT Security Relevance
[Describe how this program relates to OT security:
- Direct OT focus (ICS, SCADA, critical infrastructure)
- OT-relevant components (security architecture, risk management applicable to OT)
- Specific OT topics covered]

## Program Features
[Any notable features: hands-on labs, certifications, industry partnerships, etc.]

## Notes
[Any additional relevant information]
```

### Step 4: Update Summary Table
Update `curriculum-summary-table.md` with the new program:

**For Academic Programs:**
Add a row to the "Academic Degree Programs" table with:
- Institution
- Program Name
- Format
- Credits/Courses
- Duration
- OT Security Focus (High/Moderate/Low)
- Key Features

**For Professional Training:**
Add a row to the "Research and Training Centers" or create a new section for "Professional Training Programs" with:
- Institution
- Program/Centre Name
- Type
- OT Security Relevance
- Key Focus Areas

### Step 5: Update README
Update `README.md` to include the new program in the appropriate section:
- Academic Degree Programs
- Research and Training Centers
- Professional Training Programs

Add the program to the "OT Security Relevance" section if applicable.

### Step 6: Update Additional Programs List (Optional)
If you discover programs that need more research, add them to `additional-programs-to-research.md` with:
- Institution name
- Program name
- Potential focus
- Research status
- Notes

## Information Gathering Strategies

### Web Search Approach
1. **Start with official program pages**: Look for curriculum pages, course catalogs, program requirements
2. **Search for course lists**: Look for detailed course descriptions
3. **Check for specializations**: Many programs have tracks or focus areas
4. **Look for OT/ICS keywords**: Search for mentions of "industrial control systems", "SCADA", "critical infrastructure", "cyber-physical systems"

### Search Queries to Use
```
"[Institution] cybersecurity master's curriculum"
"[Institution] OT security training"
"[Institution] industrial control systems security"
"[Institution] ICS SCADA security courses"
"[Institution] cyber-physical systems security"
```

### Information Sources
- Official university/program websites (preferred)
- Course catalogs
- Program brochures/flyers
- Academic department pages
- Student handbooks
- Accreditation documents

## Quality Checklist

Before finalizing a program file, verify:
- [ ] Institution name is correct and complete
- [ ] Program name matches official name
- [ ] URL is valid and points to curriculum information
- [ ] Course list is complete (if available)
- [ ] OT security relevance is clearly described
- [ ] File naming follows convention
- [ ] Summary table is updated
- [ ] README is updated
- [ ] Information is accurate and current

## Common Program Types

### Academic Degree Programs
- Master's in Cybersecurity
- Master's in Information Security
- Master's in Cyber-Physical Systems
- Master's in IT Management (with cybersecurity focus)
- Graduate Certificates in OT Security

### Professional Training
- SANS ICS courses
- CERT training programs
- Vendor-specific training (Rockwell, Siemens, Schneider)
- Industry certifications (ISA/IEC 62443, GICSP)

### Research Centers
- Industrial IoT research centers
- Critical infrastructure security labs
- Cyber-physical systems research groups

## OT Security Keywords to Look For

When evaluating OT security relevance, look for mentions of:
- Industrial Control Systems (ICS)
- SCADA (Supervisory Control and Data Acquisition)
- Operational Technology (OT)
- Critical Infrastructure
- Cyber-Physical Systems
- Industrial IoT (IIoT)
- Programmable Logic Controllers (PLCs)
- Distributed Control Systems (DCS)
- Safety Instrumented Systems (SIS)
- Process Control Networks
- Industrial Network Security

## Example Workflow

1. **Identify**: "I need to research Carnegie Mellon CERT's OT security training"
2. **Search**: Use web search with queries like "Carnegie Mellon CERT ICS security training curriculum"
3. **Gather**: Collect program details, course lists, OT relevance
4. **Create File**: `carnegie-mellon-cert-ot-training.md` following the template
5. **Update Tables**: Add to summary table and README
6. **Verify**: Check all information is accurate and complete

## Notes for Future Agents

- Always verify information from official sources
- If curriculum details are incomplete, note this in the file
- Include "Last Updated" date in each file
- Maintain consistency in formatting across all files
- When in doubt about OT relevance, include the program but note the connection clearly
- Professional training programs may not have traditional "curriculum" - describe courses/training offerings instead
- Some programs may be research centers rather than training programs - document their services and focus areas

## File Naming Conventions

- Use lowercase
- Separate words with hyphens
- Include institution name and program identifier
- Keep names concise but descriptive
- Examples:
  - `georgetown-university-itm-cybersecurity.md`
  - `georgia-tech-oms-cybersecurity.md`
  - `sans-ot-security-training.md`
  - `carnegie-mellon-cert-ics-training.md`

## Last Updated
2025-01-27
