# Agent Prompt Template for Gathering Cybersecurity/OT Security Program Information

## Direct Prompt for AI Agents

Use this prompt template when asking an AI agent to gather cybersecurity and OT security program information:

---

**PROMPT:**

I need you to research and document cybersecurity and Operational Technology (OT) security training programs. Please follow these steps:

### Task
Research the following program(s) and add their curriculum information to the directory: `/Users/zak/src/projects/learning-economies/research_sources/curriculum/`

### Programs to Research
[List specific programs, URLs, or search terms here]

**Example:**
- Carnegie Mellon CERT - ICS Security Training
- Purdue University - Cybersecurity programs with OT focus
- ISA/IEC 62443 certification training programs

### Required Actions

1. **Search for program information** using web search with queries like:
   - "[Institution] cybersecurity curriculum"
   - "[Institution] OT security training"
   - "[Institution] industrial control systems security courses"

2. **For each program, gather:**
   - Institution name
   - Program name
   - Program type (Academic Degree / Professional Training / Research Centre)
   - Format (Online / On-Campus / Hybrid)
   - Total credits/courses
   - Duration
   - Official curriculum URL
   - Core courses (with course codes if available)
   - Required/foundation courses
   - Elective courses (especially OT/cybersecurity related)
   - Specializations/tracks
   - OT security relevance (direct OT focus, OT-relevant components, specific OT topics)

3. **Create a markdown file** for each program using naming convention:
   `[institution-name-lowercase]-[program-identifier].md`

   Use the template structure from existing files like `georgia-tech-oms-cybersecurity.md` or `georgetown-university-itm-cybersecurity.md`

4. **Update `curriculum-summary-table.md`** with the new program(s)

5. **Update `README.md`** to include the new program(s) in the appropriate section

6. **If programs need more research**, add them to `additional-programs-to-research.md`

### File Structure to Follow

Each program file should include:
- Program Overview (institution, program name, format, credits, duration, URL)
- Program Structure (core courses, required courses, electives, tracks)
- OT Security Relevance (how it relates to OT security)
- Program Features
- Notes

### OT Security Keywords to Identify Relevance
- Industrial Control Systems (ICS)
- SCADA
- Operational Technology (OT)
- Critical Infrastructure
- Cyber-Physical Systems
- Industrial IoT (IIoT)
- Process Control Networks

### Quality Checklist
Before completing, verify:
- [ ] All information is from official sources
- [ ] File naming follows convention (lowercase, hyphens)
- [ ] Summary table is updated
- [ ] README is updated
- [ ] OT security relevance is clearly described
- [ ] "Last Updated" date is included

---

## Example Usage

**User Prompt:**
```
I need you to research and document the following cybersecurity and OT security programs:

1. Carnegie Mellon CERT - ICS Security Training (https://www.cert.org/)
2. ISA/IEC 62443 certification programs
3. University of Tulsa - Cybersecurity programs with OT focus

Please follow the agent prompt template in the curriculum directory and add all information to the appropriate files.
```

**Agent should:**
1. Search for each program's curriculum information
2. Create individual markdown files for each
3. Update the summary table
4. Update the README
5. Verify all information is complete

## Quick Reference: Existing Files to Use as Templates

- `georgia-tech-oms-cybersecurity.md` - Academic program with OT track
- `georgetown-university-itm-cybersecurity.md` - Academic program with cybersecurity focus
- `sans-ot-security-training.md` - Professional training program
- `mohawk-college-iiot.md` - Research centre

## Notes
- Always verify information from official program websites
- If curriculum details are incomplete, note this in the file
- Maintain consistency in formatting across all files
- Professional training programs may describe courses/training offerings rather than traditional "curriculum"
