from io import StringIO

import pandas as pd

# flake8: noqa

construction_data_csv = """
id,title,identifier,publisher_id,publisher,language,format,description,date_issued,date_modified,date_valid,audience,coverage,subject,type,license,regulatory_topics,status,date_uploaded_to_orp,has_format,is_format_of,has_version,is_version_of,references,is_referenced_by,has_part,is_part_of,is_replaced_by,replaces,related_legislation
Nt6Ft0Dt,Introduction to asbestos safety,https://www.hse.gov.uk/asbestos/introduction/index.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The guidance summarises what you should do to comply with the law, including:

actions to take depending on your job role
identifying if asbestos is present and its condition
assessing the risks and putting the right controls in place
providing the right training, instruction and information to anyone who might disturb asbestos
understanding when a licensed contractor must do the work",12/09/2019,01/03/2021,01/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Risk Assessment
Lung Conditions
Safety on Site",Active,,,,,,"https://www.hse.gov.uk/asbestos/workers.htm
https://www.hse.gov.uk/asbestos/duty/index.htm
https://www.gov.uk/government/publications/asbestos-properties-incident-management-and-toxicology/asbestos-general-information
https://www.hse.gov.uk/pubns/books/l143.htm
https://www.hse.gov.uk/pubns/books/hsg227.htm
https://www.hse.gov.uk/asbestos/licensing/non-licensed-work.htm
https://www.hse.gov.uk/asbestos/licensing/licensed-contractor.htm",,,,,,"https://www.legislation.gov.uk/uksi/2012/632
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2015/51
https://www.legislation.gov.uk/uksi/2013/1471"
Sb7Oe0Yo,The Control of Substances Hazardous to Health Regulations 2002. Approved Code of Practice and guidance,https://www.hse.gov.uk/pubns/books/l5.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,The sixth edition of this Approved Code of Practice and guidance provides practical advice to help dutyholders comply with the requirements of the COSHH Regulations.,13/09/2019,12/04/2023,12/04/2023,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"COSHH
Code of Practice
Substances Hazardous to Health
",Active,,,,,,"www.hse.gov.uk/pubns/books/L24.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/hsg258.htm
https://www.hse.gov.uk/pubns/books/l8.htm
https://www.hse.gov.uk/pubns/books/eh40.htm",,,,,,"https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/ukpga/1974/37"
Ou7Ai8Hu,Legionnaires' disease. The control of legionella bacteria in water systems,https://www.hse.gov.uk/pubns/books/l8.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This book is aimed at dutyholders, including employers, those in control of premises and those with health and safety responsibilities for others, to help them comply with their legal duties in relation to legionella. These include identifying and assessing sources of risk, preparing a scheme to prevent or control risk, implementing, managing and monitoring precautions, keeping records of precautions and appointing a manager to be responsible for others.",14/09/2019,12/04/2023,12/04/2023,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39014",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Legionnaires' disease
Bacteria
Prevention
Water Systems",Active,,,,,,"www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/indg232.htm
www.hse.gov.uk/pubns/indg453.htm
www.hse.gov.uk/pubns/indg458.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1999/1148"
Yw4Ec7Ru,Provision and Use of Work Equipment Regulations 1998. Approved Code of Practice and guidance,https://www.hse.gov.uk/pubns/books/l22.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This Approved Code of Practice and guidance is aimed at employers, dutyholders and anyone who has responsibility for the safe use of work equipment, such as managers and supervisors. It sets out what is needed to comply with the Provision and Use of Work Equipment Regulations 1998. The Regulations, commonly known as PUWER, place duties on people and companies who own, operate or have control over work equipment. PUWER also places responsibilities on businesses and organisations whose employees use work equipment, whether owned by them or not.",15/09/2019,03/03/2021,03/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39015",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Safe use of equipment
Safety at work",Active,,,,,,"www.hse.gov.uk/pubns/books/l113.htm
www.hse.gov.uk/pubns/books/l24.htm
www.hse.gov.uk/pubns/books/l26.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l144.htm
www.hse.gov.uk/pubns/indg401.htm
www.hse.gov.uk/pubns/books/l112.htm
www.hse.gov.uk/pubns/books/l114.htm
www.hse.gov.uk/pubns/indg258.htm
www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/indg453.htm
www.hse.gov.uk/pubns/books/l122.htm
www.hse.gov.uk/pubns/books/l132.htm
www.hse.gov.uk/pubns/books/l143.htm
www.hse.gov.uk/pubns/hsr25.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1986/1078
https://www.legislation.gov.uk/uksi/1999/3242"
Ir2Gj4Up,Manual handling - Manual Handling Operations Regulations 1992 - Guidance on Regulations,https://www.hse.gov.uk/pubns/books/l23.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"Employers must comply with the Manual Handling Operations Regulations 1992, as amended by the Health and Safety (Miscellaneous Amendments) Regulations 2002.
The guidance explains how to avoid, assess and reduce the risk of injury from manual handling.",16/09/2019,04/03/2021,04/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39016",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Manual handling
Heavy goods at work",Active,,,,,,"www.hse.gov.uk/pubns/books/hsg65.htm
www.hse.gov.uk/pubns/indg275.htm
www.hse.gov.uk/pubns/indg232.htm
www.hse.gov.uk/pubns/indg171.htm
www.hse.gov.uk/pubns/books/hsg60.htm
www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/books/l24.htm
www.hse.gov.uk/equality-duty/equality-act-2010.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l113.htm
www.hse.gov.uk/pubns/books/l22.htm",,,,,,"https://www.legislation.gov.uk/uksi/2002/2174
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1992/2793"
Zc9Fc3Mq,Personal protective equipment at work: The Personal Protective Equipment at Work Regulations 1992 (as amended): Guidance on Regulations,https://www.hse.gov.uk/pubns/books/l25.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance explains how you can comply with the Personal Protective Equipment at Work Regulations 1992 (PPER 1992) as amended by the Personal Protective Equipment at Work (Amendment) Regulations 2022 (PPER 2022).,17/09/2019,04/03/2024,04/03/2024,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39017",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"PPE
Personal Protective Equipment",Active,,,,,,"https://www.gov.uk/government/publications/personal-protective-equipment-enforcement-regulations-2018
https://www.hse.gov.uk/pubns/indg232.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/l108.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.gov.uk/government/publications/safety-at-street-works-and-road-works
https://www.hse.gov.uk/pubns/books/l113.htm
",,,,,,"https://www.legislation.gov.uk/uksi/2022/8
https://www.legislation.gov.uk/uksi/2018/390
https://www.legislation.gov.uk/uksi/2019/696
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2012/632"
Cf6Ao5Yu,Gas Safety (Installation and Use) Regulations 1998 (GSIUR) as amended. Approved Code of Practice and guidance,https://www.hse.gov.uk/pubns/books/l56.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This Approved Code of Practice and guidance gives advice on how to meet the requirements of GSIUR and the amending regulations.

This guidance is for anyone who may have a duty under the Gas Safety (Installation and Use) Regulations 1998, including those who install, service, maintain or repair gas appliances and other gas fittings. Landlords also have duties under these regulations.",18/09/2019,04/03/2021,05/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39018",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Gas Safety
Gas Installation
Maintenance
Repair",Active,,,,,,www.hse.gov.uk/pubns/books/l22.htm,,,,,,https://www.legislation.gov.uk/uksi/2018/139
Ow5Fr0Lv,First aid at work: Guidance on regulations,https://www.hse.gov.uk/pubns/books/l74.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance is for employers. It sets out what you need to do to address first-aid provision in the workplace.,19/09/2019,06/02/2024,06/02/2024,Employers,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39019",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"First aid
Workplace first responder",Active,,,,,,"www.hse.gov.uk/pubns/indg453.htm
www.hse.gov.uk/pubns/books/l64.htm
https://books.hse.gov.uk/PUWER",,,,,,
Tb1Fu7Tu,A guide to the well aspects of the Offshore Installations and Wells (Design and Construction etc) Regulations 1996. Guidance on Regulations,https://www.hse.gov.uk/pubns/books/l84.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance reflects the six headline regulatory concerns: ensuring well risks are as low as reasonably practicable; correct assessment of subterranean conditions; proper consideration of suspension and abandonment issues; appropriate well examination schemes; provision of regular reports to the Health and Safety Executive; and promotion of competence in those undertaking well operations.,20/09/2019,19/09/2023,19/09/2023,Offshore Construction Companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Offshore installations
Oil rigs
Offshore construction",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l30.htm
https://www.hse.gov.uk/pubns/books/l65.htm
https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/l70.htm",,,,,,"https://www.legislation.gov.uk/uksi/1996/913
https://www.legislation.gov.uk/uksi/2005/3117
https://www.legislation.gov.uk/ukpga/1974/37"
Do9Fi9Fb,"Confined Spaces Regulations 1997. Approved Code of Practice, Regulations and guidance",https://www.hse.gov.uk/pubns/books/l101.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This Approved Code of Practice (ACOP) and guidance is for those involved in work within confined spaces, those who employ or train such people and those that represent them.

It explains the definition of a confined space in the Regulations and gives examples. It will help you assess the risk of working within a particular confined space and put precautions in place for work to be carried out safely.",21/09/2019,15/11/2023,15/11/2023,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39018",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Confined spaces
Safety at work
Training
Risk Prevention",Active,,,,,,"www.hse.gov.uk/pubns/books/l22.htm
www.hse.gov.uk/pubns/books/l113.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/hsg53.htm
www.hse.gov.uk/pubns/books/hsr25.htm
www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/books/l108.htm
www.hse.gov.uk/pubns/books/l143.htm
www.hse.gov.uk/pubns/books/l144.htm",,,,,,
Pl6Od1Yb,The Control of Noise at Work Regulations 2005,https://www.hse.gov.uk/pubns/books/l108.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at employers and other dutyholders and includes the Control of Noise at Work Regulations alongside guidance on what they mean, setting out an employer's legal obligations to control risks to workers' health and safety from noise.

It also gives detailed advice on assessing risks, practical noise control, how to select and use hearing protection, what to consider when buying and hiring equipment and how to develop health surveillance procedures.",22/09/2019,21/10/2021,21/10/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39019",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Noise Reduction
Noise Prevention
Noise Protection",Active,,,,,,"www.hse.gov.uk/pubns/books/l153.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l146.htm
www.hse.gov.uk/pubns/books/l110.htm
www.hse.gov.uk/pubns/books/l22.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1990/1380
https://www.legislation.gov.uk/uksi/2018/390
https://www.legislation.gov.uk/uksi/2008/1597
https://www.legislation.gov.uk/uksi/2001/1701"
Xv8Cy8Tc,A guide to the Control of Major Accident Hazards Regulations (COMAH) 2015,https://www.hse.gov.uk/pubns/books/l111.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is for anyone who has duties under the COMAH Regulations 2015, particularly operators of establishments, and also others such as local authorities and emergency planners. The aim of the Regulations is to prevent and mitigate the effects on people and the environment of major accidents involving dangerous substances. This guidance on the COMAH Regulations 2015 gives advice on the scope of the Regulations and the duties imposed by them.",23/09/2019,04/03/2021,04/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39020",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Major Accidents
Risk Prevention
Incident Response
COMAH",Active,,,,,,"www.hse.gov.uk/pubns/books/l150.htm
www.gov.uk/preparation-and-planning-for-emergencies-the-capabilities-programme",,,,,,"https://www.legislation.gov.uk/ukpga/2004/36
https://www.legislation.gov.uk/uksi/2015/483"
Se5Bm5Es,Lifting Operations and Lifting Equipment Regulations 1998. Approved Code of Practice and guidance,https://www.hse.gov.uk/pubns/books/l113.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This Approved Code of Practice and guidance is for those that work with any equipment provided at work or for the use of people at work, those who employ such people, those that represent them and those people who act as a competent person in the examination of lifting equipment.

It sets out what you should do to comply with the Lifting Operations and Lifting Equipment Regulations 1998 (LOLER).

LOLER applies to lifting equipment and builds on the requirements of the Provision and Use of Work Equipment Regulations (PUWER).",24/09/2019,04/03/2021,04/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39021",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Lifting Equipment
Work Equipment",Active,,,,,,"www.hse.gov.uk/pubns/books/l22.htm
www.hse.gov.uk/pubns/books/l23.htm
www.hse.gov.uk/pubns/books/l24.htm
www.hse.gov.uk/pubns/books/hsg221.htm
www.hse.gov.uk/pubns/hsis4.htm
www.hse.gov.uk/pubns/books/l117.htm
www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/books/hsg261.htm
www.hse.gov.uk/pubns/pm28.htm
www.hse.gov.uk/pubns/pm15.htm
www.hse.gov.uk/pubns/hsis3.htm
www.hse.gov.uk/pubns/books/l64.htm
www.hse.gov.uk/pubns/gs6.htm
www.hse.gov.uk/pubns/books/l101.htm",,,,,,"https://www.legislation.gov.uk/uksi/1998/2307
https://www.legislation.gov.uk/uksi/1998/2306"
So0Xk3Hc,Provision and Use of Work Equipment Regulations 1998 (as applied to woodworking machinery). Approved Code of Practice and guidance,https://www.hse.gov.uk/pubns/books/l114.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This Approved Code of Practice and guidance is aimed at employers, dutyholders and anyone who has responsibility for the safe use of woodworking machinery, such as managers and supervisors. It applies to most woodworking machinery, except hand-held tools, and includes tasks involving wood, corkboard, fibreboard and composite materials. It gives practical advice on the safe use of woodworking machinery and covers the provision of information and training, as well as aspects of guarding.",25/09/2019,04/03/2021,04/03/2021,"Construction companies
Metals manufacturing companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022
16210
16240",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Woodworking
Construction with wood
Wood Manufacturing",Active,,,,,,"www.hse.gov.uk/pubns/books/l22.htm
www.hse.gov.uk/pubns/wis37.htm
www.hse.gov.uk/pubns/wis16.htm
www.hse.gov.uk/pubns/wis18.htm
www.hse.gov.uk/pubns/wis38.htm
www.hse.gov.uk/pubns/wis13.htm
www.hse.gov.uk/pubns/books/hsg258.htm
www.hse.gov.uk/pubns/wis14.htm",,,,,,"https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242"
Sd1Oy2Qg,Control of lead at work (Third edition),https://www.hse.gov.uk/pubns/books/l132.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The Approved Code and accompanying guidance is aligned to the Regulations and emphasise that excessive exposure to lead has been a long-recognised health hazard. Accordingly this documents how to manage such risks and satisfy the requirements applicable to activities, eg handling, processing, repairing, maintenance, storage, disposal - liable to expose employees and others to metallic lead, its alloys and compounds (including alkyls), or when it is a component of another substance or material.",26/09/2019,19/09/2023,19/09/2023,"Construction companies
Metals manufacturing companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022
16210
16241",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Lead
Lead Allots
Lead Compounds
Managing exposure",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l24.htm
https://www.hse.gov.uk/pubns/hsc13.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/eh40.htm
https://www.hse.gov.uk/pubns/books/hsg173.htm
https://www.hse.gov.uk/pubns/indg453.htm",,,,,,https://www.legislation.gov.uk/uksi/2002/2676
Kb3Aa1Vs,Hand-arm vibration: The Control of Vibration at Work Regulations 2005,https://www.hse.gov.uk/pubns/books/l140.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance looks at the employer's legal obligations to control risks to employees' health and safety from exposure to HAV and to prevent HAV-related diseases such as hand-arm vibration syndrome and carpal tunnel syndrome. It covers the management and control of the risks from HAV and how to protect employees, with practical guidance on risk assessments, controlling vibration exposure and arranging health surveillance.",27/09/2019,04/03/2021,04/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39021",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Vibrations
Hands
Arms
Carpal-tunnel syndrome",Active,,,,,,"www.hse.gov.uk/pubns/books/l141.htm
www.hse.gov.uk/pubns/books/l153.htm
www.hse.gov.uk/pubns/books/l146.htm
www.hse.gov.uk/pubns/books/hsg263.htm
www.hse.gov.uk/pubns/books/l110.htm
www.hse.gov.uk/pubns/books/l22.htm
www.hse.gov.uk/pubns/books/l25.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2008/1597
https://www.legislation.gov.uk/uksi/1990/1380
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2007/3077"
Ku3Sl6Wc,Safety Representatives and Safety Committees Regulations 1977 (as amended) and Health and Safety (Consultation with Employees) Regulations 1996 (as amended). Approved Codes of Practice and guidance,https://www.hse.gov.uk/pubns/books/l146.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance gives you the law and guidance on how to consult and involve your employees and their representatives on health and safety matters at work under the Safety Representatives and Safety Committees Regulations 1977 (as amended) and the Health and Safety (Consultation with Employees) Regulations 1996 (as amended). It explains the relationship between the two sets of regulations and how they affect you and your workforce; in some workplaces you may have to consult under both sets of regulations.,28/09/2019,24/04/2023,24/04/2023,Employers,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Consultation
Employee Involvement",Active,,,,,,"www.hse.gov.uk/pubns/books/hsg263.htm
www.hse.gov.uk/pubns/books/l110.htm
www.hse.gov.uk/pubns/books/l144.htm
www.hse.gov.uk/pubns/books/l74.htm
www.hse.gov.uk/pubns/books/l64.htm
https://www.orr.gov.uk/guidance-compliance/rail/health-safety/laws/rogs
www.hse.gov.uk/pubns/books/l143.htm
www.hse.gov.uk/pubns/books/l132.htm
www.hse.gov.uk/pubns/books/l108.htm
www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/books/l140.htm
www.hse.gov.uk/pubns/books/l141.htm
www.hse.gov.uk/pubns/books/l26.htm
www.hse.gov.uk/pubns/books/l121.htm
www.hse.gov.uk/pubns/books/l126.htm
www.hse.gov.uk/pubns/books/l23.htm
www.hse.gov.uk/pubns/books/l22.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l72.htm
www.hse.gov.uk/pubns/books/l138.htm
www.hse.gov.uk/pubns/books/hsr27.htm
www.hse.gov.uk/pubns/books/l44.htm
www.hse.gov.uk/pubns/books/l118.htm
www.hse.gov.uk/pubns/books/l122.htm
www.hse.gov.uk/pubns/books/l96.htm
www.hse.gov.uk/pubns/books/l29.htm
www.hse.gov.uk/pubns/books/l111.htm
www.hse.gov.uk/pubns/books/L101.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/ukpga/Eliz2/2-3/70
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1995/2005/made
https://www.legislation.gov.uk/uksi/2005/1541
https://www.legislation.gov.uk/uksi/2007/1573"
Iy0Dk4Rb,Construction (Design and Management) Regulations 2015. Guidance on Regulations,https://www.hse.gov.uk/pubns/books/l153.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The Construction (Design and Management) Regulations 2015 (CDM 2015) came into force on 6 April 2015, replacing CDM 2007. This publication provides guidance on the legal requirements for CDM 2015 and is available to help anyone with duties under the Regulations. It describes:

the law that applies to the whole construction process on all construction projects, from concept to completion
what each dutyholder must or should do to comply with the law to ensure projects are carried out in a way that secures health and safety",29/09/2019,04/03/2021,04/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39021",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Construction
Design
Management
Completion
Site Safety",Active,,,,,,"www.hse.gov.uk/pubns/books/l24.htm
www.hse.gov.uk/pubns/cis59.htm",,,,,,https://www.legislation.gov.uk/uksi/2015/51
Kg6Uv0Ws,Health surveillance for those exposed to respirable crystalline silica (RCS) - Guidance for occupational health professionals,https://www.hse.gov.uk/pubns/books/healthsurveillance.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This supplement provides an example of a health surveillance programme for silicosis
for occupational health providers and employers to consider. It provides advice on:
who to include in a health surveillance programme; and
who the 'competent person' should be for carrying out each stage of the health
surveillance programme.",30/09/2019,05/03/2021,05/03/2021,Occupational health professionals,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Respirable Crystalline Silica
Occupational Health
Exposure",Active,,,,,,www.hse.gov.uk/pubns/guidance/g404.htm,,,,,,
Ga1Py1Ox,LOLER 1998 Lifting Operations and Lifting Equipment Regulations (LOLER) 1998: Open learning guidance,https://www.hse.gov.uk/pubns/books/loler.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance explains the Lifting Operations and Lifting Equipment Regulations
(LOLER) 1998. The LOLER Regulations aim to make life safer for everyone using
and coming into contact with lifting equipment.
The book describes each regulation in turn. It contains text from the regulations,
as well as case studies, key terms, activities and self-assessment questions.",01/10/2019,06/03/2021,06/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39021",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Lifting Equipment
Work Equipment",Active,,,,,,"www.hse.gov.uk/pubns/indg163.htm
https://www.hse.gov.uk/pubns/gs6.htm",,,,,,https://www.legislation.gov.uk/uksi/1998/2307
Ye8Wj1Ju,PUWER 1998: Provision and Use of Work Equipment Regulations 1998. Open learning guidance,https://www.hse.gov.uk/pubns/books/puwer.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This open learning guidance explains the Provision and Use of Work Equipment
Regulations 1998 (PUWER) to help you learn about and understand them. The
Regulations deal with the work equipment and machinery used every day in
workplaces: factories, offices, shops, hospitals, construction sites, farms -
wherever equipment and machinery is used at work.",02/10/2019,07/03/2021,07/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,Work Equipment,Active,,,,,,https://www.hse.gov.uk/pubns/books/l112.htm,,,,,,https://www.legislation.gov.uk/uksi/1998/2306
Lb4Ui1Qv,Safety in the use of abrasive wheels,https://www.hse.gov.uk/pubns/books/hsg17.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance advises on precautions you can take to prevent accidents in the use of abrasive wheels, in particular injury resulting from either wheel breakage or contact with a running wheel.",03/10/2019,08/03/2021,08/03/2021,"Construction companies
Foundry operators
Engineers",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023
24540
25500",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Abrasive Wheels
Accident Prevention
Equipment at Work",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/l25.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/l108.htm",,,,,,"https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/1992/3073
https://www.legislation.gov.uk/ukpga/1974/37"
Dp6Kt9Nh,Health and safety in roof work,https://www.hse.gov.uk/pubns/books/hsg33.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The document contains guidance on how to plan and work safely on roofs. It covers
new buildings, repair, maintenance, cleaning work and demolition. It also includes some
guidance for people not directly carrying out work on a roof, such as clients, designers
and specifiers.",04/10/2019,09/03/2021,09/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Roof Work
Working at Height
Safety Measures",Active,,,,,,"www.hse.gov.uk/pubns/books/l153.htm
http://www.hse.gov.uk/pubns/geis6.htm
http://www.hse.gov.uk/pubns/gs6.htm
http://www.hse.gov.uk/pubns/books/hsg168.htm
http://www.hse.gov.uk/pubns/guidance/a12.htm
https://www.gov.uk/dispose-hazardous-waste
www.hse.gov.uk/pubns/books/hsg151.htm
www.hse.gov.uk/pubns/books/l64.htm
www.hse.gov.uk/pubns/books/l143.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/2005/735
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2015/51
https://www.legislation.gov.uk/uksi/1998/2307"
Ps6Ir4Ka,Avoiding danger from underground services,https://www.hse.gov.uk/pubns/books/hsg47.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at all those involved in commissioning, planning, managing
and carrying out work on or near underground services. It will also be of use to the
owners and operators of such services.
It outlines the potential dangers of working near underground services and gives
advice on how to reduce any direct risks to people's health and safety, as well as
the indirect risks arising through damage to services.",05/10/2019,10/03/2021,10/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Underground Services
Electricity Lines
Gas Mains
Water Pipes
Damage to Services",Active,,,,,,"https://www.gov.uk/government/publications/safety-at-street-works-and-road-works
https://www.gov.uk/government/publications/traffic-signs-manualwww.hse.gov.uk/pubns/books/l82.htm
https://www.gov.uk/government/publications/specification-for-the-reinstatement-of-openings-in-highways
www.hse.gov.uk/pubns/hsr25.htm
www.hse.gov.uk/pubns/books/l80.htm
www.hse.gov.uk/pubns/books/l144.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/1989/635
https://www.legislation.gov.uk/uksi/2013/1471
https://www.legislation.gov.uk/uksi/1996/551
https://www.legislation.gov.uk/uksi/1996/825
https://www.legislation.gov.uk/ukpga/1991/22
https://www.legislation.gov.uk/uksi/2002/2665
https://www.legislation.gov.uk/ukpga/Geo6/10-11/41"
Mp5Zi8Ru,Reducing error and influencing behaviour,https://www.hse.gov.uk/pubns/books/hsg48.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The guidance:explains how human error and behaviour can impact on health and safety; n shows how human behaviour and other factors in the workplace can affect the n physical and mental health of workers;provides practical ideas on what you can do to identify, assess and control n risks arising from the human factor; andincludes illustrative case studies to show how other organisations have tackled n different human problems at work.",06/10/2019,11/03/2021,11/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Human Factors
Influences on humans
Human error",Active,,,,,,https://www.hse.gov.uk/pubns/books/hsg65.htm,,,,,,
In6Kj3Al,Respiratory protective equipment at work,https://www.hse.gov.uk/pubns/books/hsg53.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This book provides guidance on the selection and use of adequate and suitable
respiratory protective equipment (RPE) in the workplace, in order to comply with
the law.",07/10/2019,12/03/2021,12/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Particulates
Respiratory protection
RPE
Masks",Active,,,,,,"www.hse.gov.uk/pubns/books/l5.htm
www.hse.gov.uk/pubns/books/l101.htm
www.hse.gov.uk/pubns/indg232.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l21.htm
www.hse.gov.uk/pubns/books/l143.htm
www.hse.gov.uk/pubns/books/l132.htm
www.hse.gov.uk/pubns/books/l121.htm
www.hse.gov.uk/pubns/books/l73.htm
www.hse.gov.uk/pubns/books/eh40.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2002/2665
https://www.legislation.gov.uk/uksi/2012/632
https://www.legislation.gov.uk/uksi/2002/2676
https://www.legislation.gov.uk/uksi/1999/3232
https://www.legislation.gov.uk/uksi/1997/1713
https://www.legislation.gov.uk/uksi/1997/1713"
Wm8Ki2Vu,Respiratory protective equipment at work,https://www.hse.gov.uk/pubns/books/hsg65.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This book is mainly for leaders, owners, trustees and line managers. It will particularly help those who need to put in place or oversee their organisation's health and safety arrangements.
The advice may also help workers and their representatives, as well as health and safety practitioners and training providers.",08/10/2019,13/03/2021,13/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Health and safety
Management
Risk profiling
Worker consultation",Active,,,,,,https://www.hse.gov.uk/pubns/books/hsg48.htm,,,,,,https://www.legislation.gov.uk/uksi/1999/3242
Ji1Pk7Ua,Electricity at work: Safe working practices,https://www.hse.gov.uk/pubns/books/hsg85.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The guidance covers the key elements to consider when devising safe working
practices and is for people who carry out work on or near electrical equipment.
It includes advice for managers and supervisors who control or influence the
design, specification, selection, installation, commissioning, maintenance or
operation of electrical equipment.",09/10/2019,14/03/2021,14/03/2021,"Construction companies
Electrical engineers
Electricians",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022
43210",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Working with electricity
Electrical design
Installation
Safe practices",Active,,,,,,"www.hse.gov.uk/pubns/books/hsr25.htm
www.hse.gov.uk/pubns/books/l128.htm
www.hse.gov.uk/pubns/books/l138.htm
www.hse.gov.uk/pubns/books/l65.htm
www.hse.gov.uk/pubns/books/hsg230.htm
www.hse.gov.uk/pubns/gs6.htm
www.hse.gov.uk/pubns/books/hsg38.htm
www.hse.gov.uk/pubns/gs38.htm
www.hse.gov.uk/pubns/books/l25.htm
www.hse.gov.uk/pubns/books/l144.htm
www.hse.gov.uk/pubns/books/hsg250.htm",,,,,,
Ve2Pa9Xv,A step by step guide to COSHH assessment,https://www.hse.gov.uk/pubns/books/hsg97.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This publication gives advice and guidance to employers on assessing their activities under the Control of Substances Hazardous to Health Regulation 2002 (COSHH). It describes and explains the principles of assessment, illustrating them with extensive examples.",10/10/2019,15/03/2021,15/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"COSHH
Control of Substances Hazardous to Health
Assessment",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/l60.htm
https://www.hse.gov.uk/pubns/books/l8.htm",,,,,,https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
Lx1Mt3Po,"Maintaining portable
electrical equipment",https://www.hse.gov.uk/pubns/books/hsg107.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is for managers, electricians, technicians and users and gives
sensible advice on maintaining portable electrical equipment to prevent danger.
It covers equipment that is connected to the fixed mains supply or a locally
generated supply. It outlines a recommended maintenance plan based on a straightforward, inexpensive system of user checks, formal visual inspection and testing.",11/10/2019,16/03/2021,16/03/2021,"Construction companies
Electricians",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023
33140
43210",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Portable electronic equipment
Repair
Safe use",Active,,,,,,https://www.hse.gov.uk/pubns/books/hsr25.htm,,,,,,"https://www.legislation.gov.uk/uksi/1989/635
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1994/3260
https://www.legislation.gov.uk/uksi/2008/1597
https://www.legislation.gov.uk/uksi/1998/2306"
Ry5Qw8Gd,"Welding, flame cutting
and allied processes",https://www.hse.gov.uk/pubns/books/hsg139.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"The guidance aims to increase awareness of the potential hazards involved
and the precautions to be taken. It covers design, construction and provision
of equipment; handling and storage of gas cylinders; personal protective
equipment; operating procedures; fire precautions; examination and testing of
equipment; and special hazards and precautions in the use of fuel gases and
oxygen.",12/10/2019,17/03/2021,17/03/2021,"Construction companies
Welding companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023
25110
25290
25120
25990
33110",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Welding
Flame cutting
Gas cylinders
Fire
Maintenance",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l23.htm
https://www.hse.gov.uk/pubns/books/l25.htm
https://www.hse.gov.uk/pubns/books/l101.htm
https://www.hse.gov.uk/pubns/books/hsg250.htm",,,,,,"https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/1996/2092
https://www.legislation.gov.uk/uksi/2000/128
https://www.legislation.gov.uk/ukpga/1971/40/enacted
https://www.legislation.gov.uk/uksi/1992/2793
https://www.legislation.gov.uk/uksi/1992/2966
https://www.legislation.gov.uk/uksi/1992/3139"
Op5Di4Eq,Electrical safety on construction sites,https://www.hse.gov.uk/pubns/books/hsg141.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance explains what to do to reduce the risk of accidents involving electricity. It includes advice on safe working practices for everyone who controls or influences the design, specification, selection, installation, commissioning, maintenance or operation of electrical systems and equipment during construction activities. Practical information is given to help understand what the requirements of the relevant legislation may mean in practice.",13/10/2019,18/03/2021,18/03/2021,"Construction companies
Electrical engineers
Electricians",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022
43210",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Electrical safety
Construction
Electrical installations",Active,,,,,,"https://www.hse.gov.uk/pubns/indg370.htm
https://www.hse.gov.uk/pubns/books/hsg85.htm
https://www.hse.gov.uk/pubns/books/hsr25.htm
https://www.hse.gov.uk/pubns/gs6.htm
https://www.hse.gov.uk/pubns/books/hsg47.htm
https://www.hse.gov.uk/pubns/books/hsg107.htm",,,,,,"https://www.legislation.gov.uk/uksi/2015/51
https://www.legislation.gov.uk/uksi/1989/635
https://www.legislation.gov.uk/uksi/1998/2306"
Ub2Lg1Td,"The safe use of vehicles on construction sites: A guide for clients, designers, contractors, managers and workers involved with construction transport",https://www.hse.gov.uk/pubns/books/hsg144.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This document gives practical guidance on how to prevent vehicle accidents on construction sites. It provides information on planning and managing vehicle operations; selecting and maintaining vehicles; and safe driving and working practices. It will be useful to clients, designers, employers, managers, the self-employed, employees, safety representatives and plant hirers.",14/10/2019,19/03/2021,19/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39022",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Construction sites
Vehicles
Heavy goods vehicles
Loading vehicles",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg136.htm
https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/l146.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/uksi/2005/735
https://www.legislation.gov.uk/uksi/1992/3073
https://www.legislation.gov.uk/uksi/1998/2306"
Qb3Vv7Rn,Health and safety in construction,https://www.hse.gov.uk/pubns/books/hsg150.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This book is aimed at the small contractor but also applies to everyone involved in construction. It provides help and assistance on how to work safely on most tasks you will encounter. It will also help to identify the main causes of accidents and ill health and explains how to eliminate hazards and control risks. The guidance is simple but comprehensive. The solutions are straightforward and easy to adopt.,15/10/2019,20/03/2021,20/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39023",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Construction site
Setting up the site
Risks during construction",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg144.htm
https://www.hse.gov.uk/pubns/books/hsg168.htm
https://www.hse.gov.uk/pubns/books/hsg33.htm
https://www.hse.gov.uk/pubns/books/l113.htm
https://www.hse.gov.uk/pubns/books/hsg47.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg210.htm
https://www.hse.gov.uk/pubns/books/l140.htm
https://www.hse.gov.uk/pubns/books/hsg141.htm
https://www.hse.gov.uk/pubns/gs6.htm
https://www.hse.gov.uk/pubns/books/l101.htm
https://www.gov.uk/government/publications/safety-at-street-works-and-road-works
https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/l23.htm
https://www.hse.gov.uk/pubns/books/l108.htm
",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1994/3140
https://www.legislation.gov.uk/uksi/1996/1592
https://www.legislation.gov.uk/uksi/2005/735
https://www.legislation.gov.uk/uksi/1989/2209
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/uksi/1992/2793
https://www.legislation.gov.uk/uksi/2005/1643
https://www.legislation.gov.uk/uksi/2005/1093
https://www.legislation.gov.uk/uksi/1995/3163
https://www.legislation.gov.uk/uksi/1981/917/regulation/3
https://www.legislation.gov.uk/uksi/1998/2307
https://www.legislation.gov.uk/uksi/2002/2675
https://www.legislation.gov.uk/uksi/2002/2676
https://www.legislation.gov.uk/uksi/1983/1649
https://www.legislation.gov.uk/uksi/1999/2373
https://www.legislation.gov.uk/uksi/1997/1713
https://www.legislation.gov.uk/uksi/1989/2209
https://www.legislation.gov.uk/ukpga/1991/22
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1996/1592
https://www.legislation.gov.uk/ukpga/1969/57"
Dv9Te6Vv,"Protecting the public
Your next move",https://www.hse.gov.uk/pubns/books/hsg151.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at all those involved in construction, not only the principal contractor, but also the client, CDM co-ordinator and designer, where appropriate. It contains practical advice on how those designing, planning, maintaining and carrying out construction work can minimise the risks to those who are not involved in the construction process but may be affected.",16/10/2019,21/03/2021,21/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39024",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Public safety
Construction sites
Site perimeter
Vulnerable groups",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg97.htm",,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1999/437
https://www.legislation.gov.uk/uksi/1995/3163"
Rj8Tf9Vi,Fire safety in construction,https://www.hse.gov.uk/pubns/books/hsg168.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance aims to support those with legal duties under the Construction (Design and Management) Regulations 2015 (CDM), and under fire safety legislation, to embed good fire risk management from design through to project completion. It refers to other relevant guidance and standards so that you can build up a clear and comprehensive package.",17/10/2019,22/03/2021,22/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39024",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Fire
Fire safety
Evacuation plans
Precautions
Emergency plan
Fire prevention",Active,,,,,,"www.hse.gov.uk/pubns/books/l153.htm
www.hse.gov.uk/pubns/books/l138.htm
www.hse.gov.uk/pubns/books/hsg140.htm
www.hse.gov.uk/pubns/books/hsg250.htm
www.hse.gov.uk/pubns/books/hsg51.htm
www.hse.gov.uk/pubns/books/hsg33.htm
www.hse.gov.uk/pubns/books/hsg139.htm
www.hse.gov.uk/pubns/indg327.htm
www.hse.gov.uk/pubns/indg314.htm
www.hse.gov.uk/pubns/books/hsg47.htm
www.gov.scot/publications/building-standards-2017-non-domestic/
www.hse.gov.uk/pubns/books/l64.htm
www.gov.uk/government/publications/fire-safety-risk-assessment-sleeping-accommodation
www.gov.scot/publications/practical-fire-safety-guidance-existing-premises-sleeping-accommodation/
www.hse.gov.uk/pubns/books/hsg175.htm",,,,,,"https://www.legislation.gov.uk/uksi/2015/51
https://www.legislation.gov.uk/uksi/2005/1541
https://www.legislation.gov.uk/asp/2005/5
https://www.legislation.gov.uk/ssi/2006/456
https://www.legislation.gov.uk/uksi/2002/2776
https://www.legislation.gov.uk/ukpga/2021/24
https://www.legislation.gov.uk/uksi/2010/471
https://www.legislation.gov.uk/uksi/2013/1471
https://www.legislation.gov.uk/uksi/2022/547"
Iq6Pp7Nf,"Managing contractors
A guide for employers",https://www.hse.gov.uk/pubns/books/hsg159.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"Safe working with contractors presents a challenge, but being a smaller company has its advantages. You can be more flexible in your approach and decisions can be made more quickly. Lines of communication are shorter, usually there are not too many people involved and it is easier to know who is around.
In this guidance we aim to help you understand what you need to do and give sound practical advice for action. Working together helps everyone to work safely.",18/10/2019,23/03/2021,23/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39025",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Contractors
Contract management
Construction contracts",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg97.htm
https://www.hse.gov.uk/pubns/books/l153.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/l23.htm
https://www.hse.gov.uk/pubns/books/l25.htm",,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7"
So3Yz3Aa,Vibration solutions: Practical ways to reduce the risk of hand-arm vibration injury,https://www.hse.gov.uk/pubns/books/hsg170.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This book is aimed at managers in industry who experience problems with vibration tools, which can cause hand-arm vibration syndrome and vibration white finger. It features case studies to demonstrate how vibration levels can be reduced and by how much. It describes solutions which have been adopted by industry and how much they cost using charts, illustrations and photographs to accompany a description of the methods used.",19/10/2019,24/03/2021,24/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39025",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Hand vibrations
Vibration reduction
Injury prevention",Active,,,,,,https://www.hse.gov.uk/pubns/books/hsg47.htm,,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1992/3073"
Er7Iw4Ie,Preparing safety reports: Control of Major Accident Hazards Regulations 1999 (COMAH),https://www.hse.gov.uk/pubns/books/hsg190.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This document gives comprehensive guidance on writing a safety report for sites containing certain quantities of dangerous substances, as required by the Control of Major Accident Hazards Regulations 1999 (COMAH).
It explains to operators of top-tier sites (as defined under COMAH) what information needs to be provided in the safety report, and how it should be presented.",20/10/2019,25/03/2021,25/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39026",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"COMAH
Control of Major Accident Hazards Regulations
Emergency planning",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l111.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/hsg28.htm",,,,,,"https://www.legislation.gov.uk/uksi/1999/743
https://www.legislation.gov.uk/uksi/1994/3247"
Uy9Iz6Tx,Emergency planning for major accidents: Control of Major Accident Hazards Regulations 1999 (COMAH),https://www.hse.gov.uk/pubns/books/hsg191.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This document provides guidance for emergency planning under the Control of Major Accident Hazards Regulations 1999 (COMAH).
The guidance is aimed at those with responsibilities for emergency planning,
on-site and off-site, at major hazards establishments, including operators, local authorities, emergency services and health authorities/boards.",21/10/2019,26/03/2021,26/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39027",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"COMAH
Control of Major Accident Hazards Regulations
Safety reports",Active,,,,,,https://www.hse.gov.uk/pubns/books/l111.htm,,,,,,"https://www.legislation.gov.uk/uksi/1999/743
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/ukpga/1965/57
https://www.legislation.gov.uk/uksi/1996/825
https://www.legislation.gov.uk/uksi/1999/743
https://www.legislation.gov.uk/uksi/2009/716"
Sp4Yo0Bc,HSG201: Controlling exposure to stone dust,https://www.hse.gov.uk/pubns/books/hsg201.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance focuses on the health risks associated with the inhalation of stone dust and how to control these risks.,22/10/2019,27/03/2021,27/03/2021,"Construction companies
Stone manufacturing companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39028
23700",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Stone
stone dust
Ventilation
Respiratory protection",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/eh40.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg258.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm",,,,,,https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
Th9Gt6Dg,Technical guidance on the safe use of lifting equipment offshore,https://www.hse.gov.uk/pubns/books/hsg221.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance provides technical information for those involved in the supply, operation and control of lifting equipment in the offshore environment. It shows how to apply the Lifting Operations and Lifting Equipment Regulations 1998 (LOLER), and the Provision and Use of Work Equipment Regulations 1998 (PUWER) offshore.",23/10/2019,28/03/2021,28/03/2021,Offshore construction companies,GB,"06200
09100",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Offsahore
Oil rigs
Drilling
Lifting equipment
Offshore safety",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/eh40.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg258.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/l23.htm
https://www.hse.gov.uk/pubns/books/l113.htm
https://www.hse.gov.uk/pubns/books/l22.htm",,,,,,"https://www.legislation.gov.uk/uksi/2005/3117
https://www.legislation.gov.uk/uksi/1998/2307
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/2001/2127
https://www.legislation.gov.uk/uksi/1992/2793
https://www.legislation.gov.uk/uksi/1995/738
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1995/743"
Sm4Fq5Qp,A comprehensive guide to managing asbestos in premises,https://www.hse.gov.uk/pubns/books/hsg227.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance tells you how to prevent, or, where this is not reasonably practicable, minimise exposure to this group of workers and other employees by managing the asbestos-containing materials (known as ACMs) on your premises.",24/10/2019,29/03/2021,29/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39027",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Risk Assessment
Lung Conditions
Safety on Site
Asbestos license",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg210.htm
https://www.hse.gov.uk/pubns/books/hsg189.htm
https://www.hse.gov.uk/pubns/books/l127.htm
https://www.hse.gov.uk/pubns/books/hsg189.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1992/3004
https://www.legislation.gov.uk/uksi/1994/3140
https://www.legislation.gov.uk/uksi/2002/2675
https://www.legislation.gov.uk/uksi/1977/500
https://www.legislation.gov.uk/uksi/1996/1513
https://www.legislation.gov.uk/uksi/1983/1649"
Xl6Ru1Rh,"Keeping electrical switchgear
safe",https://books.hse.gov.uk/gemhtm/hsg230.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at owners and operators of electrical switchgear in
industrial and commercial organisations. It may also be useful to others. It will help
managers, engineers and others to understand their responsibilities and duties in
the selection, use, operation and maintenance of high-voltage switchgear. Some
knowledge of electrical switchgear and distribution systems is necessary to gain
most benefit from this document.",25/10/2019,30/03/2021,30/03/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39028",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Switchgear
Failure
Maintenance
Oil-filled switchgear
Safety
Fire limitation",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsr25.htm
https://www.hse.gov.uk/pubns/books/l143.htm
https://www.hse.gov.uk/pubns/books/l150.htm
https://www.hse.gov.uk/pubns/books/hsg85.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/2002/2665
https://www.legislation.gov.uk/uksi/2000/1043
https://www.legislation.gov.uk/ssi/2000/95"
Tk9Tq3Ei,Asbestos: The licensed contractors' guide,https://www.hse.gov.uk/pubns/books/hsg247.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at businesses holding a licence to work with asbestos, either repairing or removing asbestos-containing materials (ACMs), supervising such work, holding an ancillary licence or providing training on asbestos. Employers who carry out work with asbestos insulation, asbestos coating, and asbestos insulating board using their own employees on their own premises, who are exempted from the requirement to hold a licence, also need this guidance. It will also be useful to people awarding contracts for such work or who have other asbestos management duties.",26/10/2019,31/03/2021,31/03/2021,Construction companies licensed to work with asbestos,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39028",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Risk Assessment
Lung Conditions
Safety on Site",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg210.htm
https://www.hse.gov.uk/pubns/books/hsg189.htm
https://www.hse.gov.uk/pubns/books/hsg248.htm
https://www.hse.gov.uk/pubns/books/hsg227.htm
https://www.hse.gov.uk/pubns/books/l101.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/l25.htm
https://www.hse.gov.uk/pubns/books/hsg33.htm
https://www.legislation.gov.uk/uksi/2004/568",,,,,,"https://www.legislation.gov.uk/uksi/1983/1649
https://www.legislation.gov.uk/uksi/1977/500
https://www.legislation.gov.uk/uksi/1996/1513
https://www.legislation.gov.uk/uksi/1983/1649
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2005/894
https://www.legislation.gov.uk/ssi/2004/112
https://www.legislation.gov.uk/ukpga/1990/43"
Rq4Hh1Vo,Asbestos: The Analysts' Guide,https://www.hse.gov.uk/pubns/books/hsg248.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is for analysts involved in asbestos work and is the authoritative source of asbestos analytical procedures within Great Britain.
The guidance has been updated to take account of legal changes, findings
from HSE's interventions, and developments in analytical procedures and methodology. It provides clarification on technical and personal safety issues, especially in relation to sampling and 4-stage clearances. Information to assess the presence of asbestos in soils and made ground is included for the first time. The guidance is also designed to assist analysts in complying with the Control of Asbestos Regulations 2012. The",27/10/2019,01/04/2021,01/04/2021,Asbestos analysts,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39029",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Risk Assessment
Lung Conditions
Safety on Site
Analysis
Measurement",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l143.htm
www.hse.gov.uk/pubns/books/hsg210.htm
www.hse.gov.uk/pubns/books/hsg247.htm
www.hse.gov.uk/pubns/books/hsg264.htm
www.hse.gov.uk/pubns/books/hsg227.htm
https://www.hse.gov.uk/pubns/books/l153.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
http://www.hse.gov.uk/pubns/books/l5.htm",,,,,,"
http://www.legislation.gov.uk/uksi/2012/632
www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1977/500
https://www.legislation.gov.uk/uksi/1996/1513
http://www.legislation.gov.uk/uksi/2005/735
https://www.legislation.gov.uk/ukpga/1990/43
https://www.legislation.gov.uk/uksi/2012/811
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
http://www.legislation.gov.uk/uksi/2009/1348
https://www.legislation.gov.uk/uksi/2005/894
https://www.legislation.gov.uk/ssi/2004/112"
Vb5Gb1Zx,"The safe isolation of plant
and equipment",https://www.hse.gov.uk/pubns/books/hsg253.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This document provides guidance on how to isolate plant and equipment safely, and how to reduce the risk of releasing hazardous substances during intrusive activities such as maintenance and sampling operations. It includes a methodology for selecting 'baseline' process isolation standards and outlines preventive and risk reduction measures.",28/10/2019,02/04/2021,02/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39028",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Isolation
Plant
Equipment
Safe isolation",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/l64.htm
https://www.hse.gov.uk/pubns/books/l22.htm
https://www.hse.gov.uk/pubns/books/hsg250.htm
https://www.hse.gov.uk/pubns/books/l23.htm
https://www.hse.gov.uk/pubns/books/l5.htm
https://www.hse.gov.uk/pubns/books/l101.htm
https://www.hse.gov.uk/pubns/books/l138.htm
https://www.hse.gov.uk/pubns/books/hsg244.htm
https://www.hse.gov.uk/pubns/books/hsr25.htm
https://www.hse.gov.uk/pubns/books/hsg85.htm
https://www.hse.gov.uk/pubns/books/l121.htm",,,,,,"www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1998/2306
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/uksi/2002/2776
https://www.legislation.gov.uk/uksi/1992/2966
https://www.legislation.gov.uk/uksi/1992/2793
https://www.legislation.gov.uk/uksi/1998/2307
https://www.legislation.gov.uk/uksi/1995/743
https://www.legislation.gov.uk/uksi/1992/2885
https://www.legislation.gov.uk/uksi/1996/913
https://www.legislation.gov.uk/uksi/1995/738
https://www.legislation.gov.uk/uksi/1989/971
https://www.legislation.gov.uk/uksi/2000/128
https://www.legislation.gov.uk/uksi/1997/1713
https://www.legislation.gov.uk/uksi/1992/3004
https://www.legislation.gov.uk/uksi/1977/500
https://www.legislation.gov.uk/uksi/1996/1513
https://www.legislation.gov.uk/uksi/1999/743
https://www.legislation.gov.uk/uksi/1996/825"
Fs2Mu3Dx,Developing process safety indicators: A step-by-step guide for chemical and major hazard industries,https://www.hse.gov.uk/pubns/books/hsg254.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at senior managers and safety professionals within major
hazard organisations that wish to develop performance indicators to give improved assurance that major hazard risks are under control.
It is presumed that companies using this guide already have appropriate safety management systems, so the emphasis is on checking whether their risk controls are effective and operating as intended. The guide draws on good practice in the UK chemical sector.",29/10/2019,03/04/2021,03/04/2021,"Construction companies
Chemical handling companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39029
20130
20140
20200
20590
46750
46120",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Chemicals
Major hazards
Safety processes
Performance measurement
Risk control system",Active,,,,,,https://www.hse.gov.uk/pubns/books/hsg65.htm,,,,,,https://www.legislation.gov.uk/uksi/1999/743
Hc0Qv4Sq,Managing risks from skin exposure at work,https://www.hse.gov.uk/pubns/books/hsg262.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This is advice on assessing and managing risks concerning skin exposure, reducing contact with harmful
materials, choosing the right protective equipment and skincare products, and
checking for early signs of skin disease.",30/10/2019,04/04/2021,04/04/2021,"Construction companies
Chemical handling companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39029
20130
20140
20200
20590
46750
46121",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Skin exposure
Preventative measure
Skin diseaseducng contact
Skincare",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/l5.htm",,,,,,https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
Qo8Oc1Sp,Involving your workforce in health and safety,https://www.hse.gov.uk/pubns/books/hsg263.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guide is mainly aimed at medium to large employers. It will help them in their
legal duty to consult and involve their employees on health and safety matters.
Small businesses may find the guidance helpful, particularly the case studies.
Employees, their health and safety representatives and trade unions may also find
the guide useful.
The guide concentrates on examples of how to comply with the Safety
Representatives and Safety Committees Regulations 1977 (as amended), and the
Health and Safety (Consultation with Employees) Regulations 1996 (as amended).
A complementary guide, containing both sets of regulations, and a leaflet are also
available.",31/10/2019,05/04/2021,05/04/2021,"Construction companies
",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39028",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Health and safety
Workforce management
Employee consultation",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l146.htm
https://www.hse.gov.uk/pubns/books/l110.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm",,,,,,"https://www.legislation.gov.uk/uksi/1977/500
https://www.legislation.gov.uk/uksi/1996/1513"
Dh9Re1Sw,Asbestos: The survey guide,https://www.hse.gov.uk/pubns/books/hsg264.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance is aimed at people
carrying out asbestos surveys and people with specific responsibilities for managing
asbestos in non-domestic premises under the Control of Asbestos Regulations
2012. The book covers competence and quality assurance and surveys, including:
survey planning, carrying out surveys, the survey report and the dutyholder's use of
the survey information. It includes extensive appendices and references.",01/11/2019,06/04/2021,06/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39029",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Surveys
Reporting",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l143.htm
https://www.hse.gov.uk/pubns/books/l153.htm
https://www.hse.gov.uk/pubns/books/hsg247.htm
https://www.hse.gov.uk/pubns/books/hsg248.htm",,,,,,"https://www.legislation.gov.uk/eur/2006/1907
https://www.legislation.gov.uk/uksi/2012/632
https://www.legislation.gov.uk/ukpga/1974/37"
Ba6Ba4Jj,Legionnaires' disease: Technical guidance Part 1,https://www.hse.gov.uk/pubns/books/hsg274part1.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance gives practical advice on the legal requirements of the Health
and Safety at Work etc Act 1974, the Control of Substances Hazardous to
Health Regulations 2002 (as amended) concerning the risk from exposure
to legionella, and guidance on compliance with the relevant parts of the
Management of Health and Safety at Work Regulations 1999.",02/11/2019,07/04/2021,07/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39030",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Legionnaires' disease
Bacteria
Prevention
Water Systems
Cooling systems",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l8.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/hsg220.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1992/2225
https://www.legislation.gov.uk/uksi/1999/1148
https://www.legislation.gov.uk/uksi/2009/3101
https://www.legislation.gov.uk/wsi/2010/66
https://www.legislation.gov.uk/ssi/2006/209
https://www.legislation.gov.uk/uksi/2000/3184
https://www.legislation.gov.uk/ukpga/1991/56
https://www.legislation.gov.uk/ukpga/1980/45
https://www.legislation.gov.uk/wsi/2010/994
https://www.legislation.gov.uk/ssi/2001/207
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/uksi/2010/659
https://www.legislation.gov.uk/
asp/2008/5
https://www.legislation.gov.uk/uksi/2010/659"
Bn7Qq8Kz,Legionnaires' disease: Technical guidance Part 2,https://www.hse.gov.uk/pubns/books/hsg274part2.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance gives practical advice on the legal requirements of the Health
and Safety at Work etc Act 1974, the Control of Substances Hazardous to
Health Regulations 2002 (as amended) concerning the risk from exposure
to legionella, and guidance on compliance with the relevant parts of the
Management of Health and Safety at Work Regulations 1999.",03/11/2019,08/04/2021,08/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39031",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Legionnaires' disease
Bacteria
Prevention
Water Systems
Cooling systems",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l8.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/hsg220.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1992/2225
https://www.legislation.gov.uk/uksi/1999/1148
https://www.legislation.gov.uk/uksi/2009/3101
https://www.legislation.gov.uk/wsi/2010/66
https://www.legislation.gov.uk/ssi/2006/209
https://www.legislation.gov.uk/uksi/2000/3184
https://www.legislation.gov.uk/ukpga/1991/56
https://www.legislation.gov.uk/ukpga/1980/45
https://www.legislation.gov.uk/wsi/2010/994
https://www.legislation.gov.uk/ssi/2001/207
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/uksi/2010/659
https://www.legislation.gov.uk/
asp/2008/5
https://www.legislation.gov.uk/uksi/2010/660"
Pg7Ck4Ly,Legionnaires' disease: Technical guidance Part 3,https://www.hse.gov.uk/pubns/books/hsg274part3.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This guidance gives practical advice on the legal requirements of the Health
and Safety at Work etc Act 1974, the Control of Substances Hazardous to
Health Regulations 2002 (as amended) concerning the risk from exposure
to legionella, and guidance on compliance with the relevant parts of the
Management of Health and Safety at Work Regulations 1999.",04/11/2019,09/04/2021,09/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39032",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Legionnaires' disease
Bacteria
Prevention
Water Systems
Cooling systems",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l8.htm
https://www.hse.gov.uk/pubns/books/hsg53.htm
https://www.hse.gov.uk/pubns/books/hsg220.htm",,,,,,"https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2002/2677/regulation/7
https://www.legislation.gov.uk/uksi/1999/3242
https://www.legislation.gov.uk/uksi/1992/2225
https://www.legislation.gov.uk/uksi/1999/1148
https://www.legislation.gov.uk/uksi/2009/3101
https://www.legislation.gov.uk/wsi/2010/66
https://www.legislation.gov.uk/ssi/2006/209
https://www.legislation.gov.uk/uksi/2000/3184
https://www.legislation.gov.uk/ukpga/1991/56
https://www.legislation.gov.uk/ukpga/1980/45
https://www.legislation.gov.uk/wsi/2010/994
https://www.legislation.gov.uk/ssi/2001/207
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/ssi/2010/95
https://www.legislation.gov.uk/uksi/2010/659
https://www.legislation.gov.uk/
asp/2008/5
https://www.legislation.gov.uk/uksi/2010/661"
Gu7Ut3Ws,"Asbestos licence assessment, amendment and revocation guide (ALAARG)",https://www.hse.gov.uk/pubns/hse50.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,"This document provides guidance on the asbestos licensing system. It should be read together with the other documents referred to. This guide is primarily for regulators, but will be of interest to others involved with licensed asbestos work, including licence holders, applicants and clients.",05/11/2019,09/04/2021,09/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39033",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Asbestos
Licensing
Asbestos Licensing Unit",Active,,,,,,"https://www.hse.gov.uk/pubns/books/l143.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/hsg247.htm",,,,,,https://www.legislation.gov.uk/uksi/2012/632
Wk3Bf7Ri,The Electricity at Work Regulations 1989,https://www.hse.gov.uk/pubns/books/hsr25.htm,healthandsafetyexecutive,Health and Safety Executive,eng,HTML,This guidance sets out the Regulations and gives technical and legal guidance on them. The purpose of this guidance is to highlight the nature of the precautions in general terms to help dutyholders achieve high standards of electrical safety in compliance with the duties imposed.,06/11/2019,09/04/2021,09/04/2021,Construction companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39034",Guidance,https://www.hse.gov.uk/help/copyright.pdf,"Electricty at Work
Electrical Safety
Insulation
Conductors",Active,,,,,,"https://www.hse.gov.uk/pubns/books/hsg278.htm
https://www.hse.gov.uk/pubns/books/hsg65.htm
https://www.hse.gov.uk/pubns/books/hsg85.htm
https://www.hse.gov.uk/pubns/books/l138.htm
https://www.hse.gov.uk/pubns/books/l74.htm
https://www.hse.gov.uk/pubns/books/hsg47.htm
https://www.hse.gov.uk/pubns/books/hsg38.htm",,,,,,"https://www.legislation.gov.uk/uksi/1989/635
https://www.legislation.gov.uk/ukpga/1974/37
https://www.legislation.gov.uk/uksi/2013/240"
Lk4Kj4Xb,Guidance for licensing under the SIA and OSA,https://www.caa.co.uk/space/guidance-and-resources/guidance-for-licensing-under-the-sia-and-osa/,civilaviationauthority,Civil Aviation Authority,eng,HTML,Further licensing information under the Space Industry Act 2018 and the Outer Space Act 1986,07/11/2019,09/04/2021,09/04/2021,Space industry operators,GB,"51220
33160
30300",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Space Industry
Licensing
Training Requirements
Orbital Operations",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap2209/
https://www.caa.co.uk/our-work/publications/documents/content/cap2221/
https://www.caa.co.uk/CAP2214
https://www.caa.co.uk/CAP2219
https://www.caa.co.uk/CAP2224",,,,,,"https://www.legislation.gov.uk/ukpga/2018/5
https://www.legislation.gov.uk/ukpga/1986/38"
Wc3Ug8Tt,Required safety information,https://www.caa.co.uk/space/guidance-and-resources/required-safety-information/,civilaviationauthority,Civil Aviation Authority,eng,HTML,Drafting a safety case and why you need one for your licence application,08/11/2019,09/04/2021,09/04/2021,Space industry operators,GB,"51220
33160
30301",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Space Industry
Licensing
Health & Safety
Orbital Operations",Active,,,,,,"https://www.hse.gov.uk/simple-health-safety/risk/index.htm
https://www.hse.gov.uk/landuseplanning/hazardoussubstances.htm
https://www.caa.co.uk/media/v55lxgda/understanding-comah-new-entrants.htm
https://www.hse.gov.uk/explosives/index.htm",,,,,,https://www.legislation.gov.uk/ukpga/2018/5
Wc0Iu8Lv,Environmental requirements,https://www.caa.co.uk/space/guidance-and-resources/environmental-requirements/,civilaviationauthority,Civil Aviation Authority,eng,HTML,"Guidance on the Assessment of Environmental Effects (AEE), environmental objectives and public consultation",09/11/2019,09/04/2021,09/04/2021,Space industry operators,GB,"51220
33160
30302",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Space Industry
Environmental impacts",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap2215/
https://www.gov.uk/government/consultations/commercial-spaceflight-environmental-objectives-for-the-spaceflight-regulator/outcome/draft-guidance-to-the-regulator-on-environmental-objectives-under-the-space-industry-act-2018-final-outcome",,,,,,https://www.legislation.gov.uk/ukpga/2018/6
Ba0Re3Ju,Planning consultations,https://www.caa.co.uk/commercial-industry/airspace/event-and-obstacle-notification/planning-consultations/,civilaviationauthority,Civil Aviation Authority,eng,HTML,Guidance on the Civil Aviation Authority (CAA) role in planning consultations relating to proposed developments in the UK,10/11/2019,09/04/2021,09/04/2021,Aviation infratsructure developers,GB,"42990
41201",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Planning
Infrastructure",Active,,,,,,"https://www.caa.co.uk/commercial-industry/airspace/event-and-obstacle-notification/obstacles-overview/
https://www.caa.co.uk/our-work/publications/documents/content/cap1096/
",,,,,,https://www.legislation.gov.uk/ukpga/2011/20/section/110
As1Oj9Dz,What is safeguarding?,https://www.caa.co.uk/combined-aerodrome-safeguarding-team-cast/what-is-safeguarding/,civilaviationauthority,Civil Aviation Authority,eng,HTML,"Aerodrome Safeguarding ensures the safety of aircraft manoeuvring on the ground, taking off, landing or flying in the vicinity of the aerodrome.",11/11/2019,09/04/2021,09/04/2021,Aerodrome operators,GB,"52102
52230
52242",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Aerodrome Safety
Health & Safety",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap-738/
https://www.caa.co.uk/publication/pid/11061
https://knowledge.bsigroup.com/products/design-of-road-lighting-lighting-of-roads-and-public-amenity-areas-code-of-practice?version=tracked
https://www.caa.co.uk/our-work/publications/documents/content/cap-736/
https://www.caa.co.uk/our-work/publications/documents/content/cap-764/
https://www.caa.co.uk/our-work/publications/documents/content/cap-772/
https://www.caa.co.uk/our-work/publications/documents/content/cap1096/",,,,,,https://www.legislation.gov.uk/uksi/2016/765/
Sb9Lo2Vj,Lighting and marking of obstacles,https://www.caa.co.uk/commercial-industry/airspace/event-and-obstacle-notification/lighting-and-marking-of-obstacles/,civilaviationauthority,Civil Aviation Authority,eng,HTML,Guidance on the requirements and recommendations for the lighting/marking of obstacles in UK airspace,12/11/2019,09/04/2021,09/04/2021,Aerodrome operators,GB,"52102
52230
52243",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,Aerodrome Safety,Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap-168/
https://www.caa.co.uk/our-work/publications/documents/content/cap1096/
https://www.caa.co.uk/our-work/publications/documents/content/cap-764/",,,,,,https://www.legislation.gov.uk/uksi/2016/765/
Ro8De5Ng,CAP 437: Standards for offshore helicopter landing areas,https://www.caa.co.uk/our-work/publications/documents/content/cap-437/,civilaviationauthority,Civil Aviation Authority,eng,HTML,This publication provides the criteria applied by the CAA in assessing the standards of offshore helicopter landing areas for worldwide use by helicopters registered in the United Kingdom.,13/11/2019,09/04/2021,09/04/2021,Helicopter Operators,GB,"51101
51102
51211",Mandatory Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Aerodrome Safety
Airline operations
Airline Safety",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap-168/
https://www.caa.co.uk/our-work/publications/documents/content/cap-413/
https://www.caa.co.uk/our-work/publications/documents/content/cap-452/
https://www.caa.co.uk/our-work/publications/documents/content/cap-670/
https://www.caa.co.uk/our-work/publications/documents/content/cap-746/
https://www.caa.co.uk/our-work/publications/documents/content/cap-764/
",,,,,,"https://www.legislation.gov.uk/ukpga/2012/19/
https://www.legislation.gov.uk/ukpga/1992/15/"
Ye7Cn2Ls,CAP 738: Safeguarding of Aerodromes,https://www.caa.co.uk/our-work/publications/documents/content/cap-738/,civilaviationauthority,Civil Aviation Authority,eng,HTML,"This document offers guidance to those responsible for the safe operation of an aerodrome or a technical site, to help them assess what impact a proposed development or construction might have on that operation.",14/11/2019,09/04/2021,09/04/2021,Aerodrome Operators,GB,"52102
52230",Mandatory Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Aerodrome Safety
Airline Safety
Airspace
General Aviation",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap-168/
https://www.caa.co.uk/our-work/publications/documents/content/cap-232/
https://www.caa.co.uk/our-work/publications/documents/content/cap1096/",,,,,,https://www.legislation.gov.uk/ukpga/2000/38/
Mw1Hl3Gh,CAP1096: Guidance to crane users on the crane notification process and obstacle lighting and marking,https://www.caa.co.uk/our-work/publications/documents/content/cap1096/,civilaviationauthority,Civil Aviation Authority,eng,HTML,"CAP 1096 provides guidance to crane users on the crane notification process and lighting and marking requirements applicable to cranes. In the main, crane-related issues are considered and managed in much the same way as for any tall object, however due to the distinctive character of the crane construction and operations, they are addressed separately.",15/11/2019,09/04/2021,09/04/2021,"Construction companies
Crane operators",GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999",Guidance,https://www.caa.co.uk/Our-work/Information-requests/Copyright-information,"Aerodrome Safety
Crane Operation
Airline Safety
Airspace",Active,,,,,,"https://www.caa.co.uk/our-work/publications/documents/content/cap-738/
https://www.caa.co.uk/our-work/publications/documents/content/cap-168/",,,,,,
Yb1Of7Ux,U1 waste exemption: use of waste in construction,https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction,environmentagency,Environment Agency,eng,HTML,The U1 exemption allows you to use suitable waste in construction as a recovery activity.,16/11/2019,09/04/2021,09/04/2021,Construction companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38110",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/government/publications/the-meaning-of-place-under-the-new-waste-exemption-system
https://www.gov.uk/guidance/waste-exemption-u8-using-waste-for-a-specified-purpose
https://www.gov.uk/guidance/waste-exemption-t5-screening-and-blending-waste
https://www.gov.uk/guidance/waste-exemption-t6-treating-waste-wood-and-waste-plant-matter-by-chipping-shredding-cutting-or-pulverising
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/waste-recovery-plans-and-deposit-for-recovery-permits
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/check-if-your-waste-is-suitable-for-deposit-for-recovery
https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation",https://www.gov.uk/guidance/waste-exemption-u2-use-of-baled-end-of-life-tyres-in-construction,,,,,
Gv1Kb6Ti,U2 waste exemption: use of baled end-of-life tyres in construction,https://www.gov.uk/guidance/waste-exemption-u2-use-of-baled-end-of-life-tyres-in-construction,environmentagency,Environment Agency,eng,HTML,The U2 exemption allows you to use a small number of end-of-life tyre bales in construction.,28/04/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38111",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Tyres",Active,,,,,,"https://www.gov.uk/guidance/waste-exemptions-using-waste
https://www.gov.uk/guidance/waste-exemption-t8-mechanically-treating-end-of-life-tyres
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Zp7Za0Xc,U3 waste exemption: construction of entertainment or educational installations,https://www.gov.uk/guidance/waste-exemption-u3-construction-of-entertainment-or-educational-installations,environmentagency,Environment Agency,eng,HTML,"The U3 exemption allows groups such as schools, colleges and theatres to use waste, such as offcuts of wood, for creative installations.",28/04/2014,09/04/2021,09/04/2021,"Schools
Colleges
Theatres",GB-ENG,"85100
85200
85310
85320
85410
85421
85422
85510
85520
85590
85600
90010
90020
90040",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Education",Active,,,,,,https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits,,,,,,
Fy8Iq9Uf,Standard Rules SR2010 No7: 50Kte Use of waste in construction (Applies to existing permit holders from 10 July 2019),https://www.gov.uk/government/publications/sr2010-no7-50kte-use-of-waste-in-construction,environmentagency,Environment Agency,eng,HTML,Standard rules for using waste in construction (existing permits only).,25/06/2012,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38111",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact",Superseded,,,,https://assets.publishing.service.gov.uk/media/5c9cb48340f0b633f3d4b74c/SR2010_No7_50kte_use_of_waste_in_construction.pdf,,https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation,,,,https://assets.publishing.service.gov.uk/media/5c9c8b82ed915d07ac4243c6/SR2015_No39_use_of_waste_in_a_deposit_for_recovery_operation.pdf,,
Uu0Os3Tr,SR2010 No 7: 50kte use of waste in construction (Applies to existing permits until 9 July 2019),https://www.gov.uk/government/publications/sr2010-no7-50kte-use-of-waste-in-construction,environmentagency,Environment Agency,eng,HTML,Standard rules for using waste in construction (existing permits only).,25/06/2012,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38112",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact",Superseded,,,,https://assets.publishing.service.gov.uk/media/5cacb55aed915d3a7a0c1409/SR2010_No7.pdf,,https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation,,,,https://assets.publishing.service.gov.uk/media/5c9c8b82ed915d07ac4243c6/SR2015_No39_use_of_waste_in_a_deposit_for_recovery_operation.pdf,,
Sb3He1Sq,SR2010 No 8: use of waste in construction,https://www.gov.uk/government/publications/sr2010-number-8-use-of-waste-in-construction,environmentagency,Environment Agency,eng,HTML,Standard rules for the storage and use of up to 100ktd of waste for construction (existing permits only).,25/06/2012,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38113",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact",Superseded,,,,,,https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation,,,,https://assets.publishing.service.gov.uk/media/5c9c8b82ed915d07ac4243c6/SR2015_No39_use_of_waste_in_a_deposit_for_recovery_operation.pdf,,
Qd1Xk4Dh,SR2010 No 13: use of waste to manufacture timber or construction products,https://www.gov.uk/government/publications/sr2010-number-13,environmentagency,Environment Agency,eng,HTML,SR2010 No 13: use of waste to manufacture timber or construction products.,09/08/2012,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38114",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact
Timber",Active,,,,,,,,,,,,
Or1Zu9Kr,SR2015 No 24: use of waste to manufacture timber or construction products,https://www.gov.uk/government/publications/sr2015-no24-use-of-waste-to-manufacture-timber-or-construction-products,environmentagency,Environment Agency,eng,HTML,"These standard rules allow you to store waste at a specified location and use it for manufacturing timber or construction products. Permitted wastes do not include hazardous wastes.

The total quantity of waste that can be stored and treated at the site under these standard rules is no more than 75,000 tonnes per year.

These standard rules do not permit the burning of any wastes, either in the open, inside buildings or in any form of incinerator.",01/12/2015,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38115",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact
Timber",Active,,,,,,https://www.gov.uk/guidance/apply-for-a-standard-rules-environmental-permit,,,,,,
Yc1Wy9Ga,Using unbound incinerator bottom ash aggregate (IBAA) in construction activities: RPS 247,https://www.gov.uk/government/publications/using-unbound-incinerator-bottom-ash-aggregate-ibaa-in-construction-activities-rps-247/using-unbound-incinerator-bottom-ash-aggregate-ibaa-in-construction-activities-rps-247,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position on when you can use unbound municipal IBAA in construction activities without an environmental permit.,29/01/2021,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38116",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Environmental Impact
Aggregate",Active,,,,,,"https://www.gov.uk/government/publications/using-unbound-incinerator-bottom-ash-aggregate-ibaa-in-construction-activities-rps-247
https://www.gov.uk/managing-your-waste-an-overview
https://www.gov.uk/dispose-hazardous-waste
https://www.gov.uk/guidance/groundwater-source-protection-zones-spzs
https://knowledge.bsigroup.com/products/aggregates-for-unbound-and-hydraulically-bound-materials-for-use-in-civil-engineering-work-and-road-construction/standard",,,,,,
Pr6Hi8Rp,SR2015 No 27: constructing an outfall pipe up to 500mm diameter through a headwall into a main river,https://www.gov.uk/government/publications/sr2015-no27-constructing-an-outfall-pipe-of-300mm-to-500mm-diameter,environmentagency,Environment Agency,eng,HTML,Standard rules for constructing an outfall pipe up to 500mm diameter through a headwall into a main river.,06/04/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"River maintenance
Flooding
Coastal Erosion
Environmental Impact",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1981/69
https://www.legislation.gov.uk/ukpga/2000/37/"
Br7Sg1Gg,Treating and using water that contains concrete and silt at construction sites: RPS 235,https://www.gov.uk/government/publications/treating-and-using-water-that-contains-concrete-and-silt-at-construction-sites-rps-235/treating-and-using-water-that-contains-concrete-and-silt-at-construction-sites-rps-235,environmentagency,Environment Agency,eng,HTML,"
If you comply with the conditions in this regulatory position statement (RPS) you can treat and use water that contains concrete and silt at construction sites without an environmental permit for a waste operation.This RPS allows you to:

store and treat water that contains concrete and silt, within the construction site, before use
use treated water that contains concrete for washing equipment or mixing concrete
use treated water that contains silt produced from washing equipment for washing equipment or damping down haul roads",21/09/2020,09/04/2021,09/04/2021,"Construction Companies
Water treatment companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38118",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental permits
Waste
Water industry",Active,,,,,,"https://www.gov.uk/government/publications/temporary-dewatering-from-excavations-to-surface-water
https://www.gov.uk/guidance/discharges-to-surface-water-and-groundwater-environmental-permits",,,,,,
Hq2Pv9Hx,T5 waste exemption: screening and blending waste,https://www.gov.uk/guidance/waste-exemption-t5-screening-and-blending-waste,environmentagency,Environment Agency,eng,HTML,"The T5 exemption allows you to temporarily treat waste on a small scale to produce aggregate or soil at a particular location, such as a construction or demolition site.",28/04/2014,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Demolition",Active,,,,,,"https://www.gov.uk/guidance/check-if-your-material-is-waste
https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction
https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction
https://www.gov.uk/guidance/waste-environmental-permits
https://www.gov.uk/how-to-classify-different-types-of-waste",,,,,,https://www.legislation.gov.uk/uksi/2010/675/schedule/3/made
Yf4Qt2Nb,Pollution prevention for businesses,https://www.gov.uk/guidance/pollution-prevention-for-businesses,environmentagency,Environment Agency,eng,HTML,"How businesses and organisations can avoid causing pollution from oil and chemical storage, car washing, construction and other activities.",12/07/2016,09/04/2021,09/04/2021,"Construction Companies
Chemical Storage Companies
Car Washing Companies
Companies handling polluting or hazardous materials",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
20130
20140
20200
20590
46120
46750",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Pollution
Environmental Impact",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/guidance/access-the-public-register-for-environmental-information
https://www.gov.uk/guidance/construction-products-regulation-in-great-britain
https://www.hse.gov.uk/pubns/books/l111.htm
https://www.hse.gov.uk/pubns/books/hsr29.htm
https://www.gov.uk/government/publications/temporary-dewatering-from-excavations-to-surface-water",,,,,,
Hf9Us6Yr,"Low risk waste positions: construction, demolition and dredging waste, aggregates and soils",https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils,environmentagency,Environment Agency,eng,HTML,"This low risk waste position (LRWP) applies if you store waste plasterboard.

If you follow the conditions in this LRWP you can carry out the activity without an environmental permit for a waste operation.",20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Waste Disposal Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38118",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Water industry
Environmental Impact",Active,,,,,,"https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-waste-plasterboard-lrwp-6
https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-and-using-waste-clay-to-make-cob-blocks-lrwp-32
https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-waste-bitumen-at-depots-for-recovery-elsewhere-lrwp-38
https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/recovery-of-wastewater-containing-soils-from-pipe-laying-excavations-lrwp-46
https://www.gov.uk/government/publications/treating-and-using-water-that-contains-concrete-and-silt-at-construction-sites-rps-235/treating-and-using-water-that-contains-concrete-and-silt-at-construction-sites-rps-235",,,,,,
Pe2Zq2Cy,Storing waste plasterboard: LRWP 6,https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-waste-plasterboard-lrwp-6,environmentagency,Environment Agency,eng,HTML,The Environment Agency has provided these low risk waste positions (LRWPs) for waste operations that it considers may be suitable for an exemption.,20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Waste Disposal Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Water industry
Environmental Impact
Plasterboard",Active,,,,,,,,,,,,
Zw5Nv1Bb,Storing and using waste clay to make cob blocks: LRWP 32,https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-and-using-waste-clay-to-make-cob-blocks-lrwp-32,environmentagency,Environment Agency,eng,HTML,This low risk waste position (LRWP) applies if you store waste clay before making cob blocks.,20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Waste Disposal Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Water industry
Environmental Impact
Clay",Active,,,,,,,,,,,,
Ao7Rg4Ko,Storing waste bitumen at depots for recovery elsewhere: LRWP 38,https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/storing-waste-bitumen-at-depots-for-recovery-elsewhere-lrwp-38,environmentagency,Environment Agency,eng,HTML,"This low risk waste position (LRWP) applies if you store waste bitumen at depots for recovery elsewhere (List of Waste code 17 03 02).

If you follow the conditions in this LRWP you can carry out the activity without an environmental permit for a waste operation.",20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Waste Disposal Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Water industry
Environmental Impact
Bitumen",Active,,,,,,,,,,,,
Zl9Gv3En,Recovery of wastewater containing soils from pipe-laying excavations: LRWP 46,https://www.gov.uk/government/publications/low-risk-waste-positions-construction-demolition-and-dredging-waste-aggregates-and-soils/recovery-of-wastewater-containing-soils-from-pipe-laying-excavations-lrwp-46,environmentagency,Environment Agency,eng,HTML,"This low risk waste position (LRWP) applies if you recover wastewater containing soils from pipe-laying excavations.

If you follow the conditions in this LRWP you can carry out the activity without an environmental permit for a waste operation.",20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Waste Disposal Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Water industry
Environmental Impact
Wastewater
Pipe Laying",Active,,,,,,,,,,,,
Sp4Px6Kq,Earthworks in landfill engineering: LFE4,https://www.gov.uk/government/publications/earthworks-in-landfill-engineering-lfe4,environmentagency,Environment Agency,eng,HTML,"This document provides guidance on the approach to the earthworks used in landfill construction. It deals with the issues relating to the design, construction and validation of earthworks for landfill sites - not just clay liners but also the cut and fill slopes required in the formation of the landfill cells, lagoons, ramps and bunds.",23/06/2014,09/04/2021,09/04/2021,"Construction Companies
Engineering Companies",GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Earthworks",Active,,,,,,"https://www.gov.uk/government/publications/using-geomembranes-in-landfill-engineering-lfe5
https://knowledge.bsigroup.com/products/eurocode-7-geotechnical-design-general-rules?version=standard
https://knowledge.bsigroup.com/products/eurocode-7-geotechnical-design-ground-investigation-and-testing?version=standard
https://knowledge.bsigroup.com/products/geotechnical-investigation-and-testing-sampling-methods-and-groundwater-measurements-technical-principles-for-execution?version=standard",,,,,,https://www.legislation.gov.uk/ukpga/1990/43/
Fc0Ed0Cy,"Planning, designing and building water storage reservoirs",https://www.gov.uk/government/publications/planning-designing-and-building-water-storage-reservoirs,environmentagency,Environment Agency,eng,HTML,"How to plan, design, construct and commission a water storage reservoir and comply with the law.",01/05/2008,09/04/2021,09/04/2021,"Construction Companies
Water Companies",GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
42990
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Impact
Water
Sewerage
Water Industry",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1975/23
https://www.legislation.gov.uk/ukpga/1991/57/
https://www.legislation.gov.uk/uksi/1995/418/"
Ur9Va2Lb,Use of clay in slurry lagoons or irrigation reservoirs: RPS 91,https://www.gov.uk/government/publications/use-of-clay-in-slurry-lagoons-or-irrigation-reservoirs-rps-91,environmentagency,Environment Agency,eng,HTML,Environment Agency regulatory position on using waste clay in the construction of slurry lagoons or irrigation/winter storage reservoirs.,05/12/2017,09/04/2021,09/04/2021,"Construction Companies
Water Companies",GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
42990
42911",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Impact
Water
Sewerage
Water Industry",Active,,,,,,https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction,,,,,,"https://www.legislation.gov.uk/uksi/2010/639
https://www.gov.uk/guidance/storing-silage-slurry-and-agricultural-fuel-oil
https://www.legislation.gov.uk/ukpga/1975/23
https://www.legislation.gov.uk/ukpga/2010/29/"
Wo7St3Yv,"SR2019 No 2: steps, ramps and other similar structures excavated into the existing bank profile of a main river","https://www.gov.uk/government/publications/sr2019-no-2-steps-ramps-and-other-similar-structures-excavated-into-the-existing-bank-profile-of-a-main-river#:~:text=These%20rules%20allow%20you%20to,metres%20of%20a%20flood%20defence",environmentagency,Environment Agency,eng,HTML,"These rules allow you to construct steps, ramps and other similar structures excavated into the existing bank profile of a main river.",01/08/2019,09/04/2021,09/04/2021,"Construction Companies
Water Infrastructure Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"River maintenance
Flooding
Coastal Erosion
Environmental Impact",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1981/69
https://www.legislation.gov.uk/ukpga/2000/37/"
Vv2Zy2Jw,Using non woven protector geotextiles in landfill engineering: LFE7,https://www.gov.uk/government/publications/using-non-woven-protector-geotextiles-in-landfill-engineering-lfe7,environmentagency,Environment Agency,eng,HTML,Guidance on the use of non woven geotextiles in landfill engineering - from design testing through to construction quality assurance.,24/06/2014,09/04/2021,09/04/2021,"Construction Companies
Engineering Companies",GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Earthworks",Active,,,,,,"https://www.gov.uk/government/publications/cylinder-testing-geomembranes-and-their-protective-materials-lfe2
https://knowledge.bsigroup.com/products/geotextiles-and-geotextile-related-products-characteristics-required-for-use-in-solid-waste-disposals?version=tracked
https://knowledge.bsigroup.com/products/geosynthetics-symbols-and-pictograms?version=standard",,,,,,
Ek7Fd5Za,SR2015 No 39: use of waste in a deposit for recovery operations,https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation,environmentagency,Environment Agency,eng,HTML,"These standard rules allow you to store and use waste in a deposit for recovery activities involving construction, reclamation, restoration or improvement of land other than by mobile plant.

These standard rules are for the recovery of waste only and do not apply to any activities involving disposal.",01/02/2016,09/04/2021,09/04/2021,"Construction Companies
",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1981/69
https://www.legislation.gov.uk/ukpga/2000/37/"
Qa5Nz6Da,Storing and using clean CRT screen glass in bound applications: RPS 188,https://www.gov.uk/government/publications/storing-and-using-clean-crt-screen-glass-in-bound-applications-rps-188/storing-and-using-crt-screen-glass-in-bound-applications-rps-188,environmentagency,Environment Agency,eng,HTML,Environment Agency regulatory position on when you can store and bind crushed clean CRT screen glass or store and use the bound glass material in construction.,12/09/2023,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38118",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Glass",Active,,,,,,,,,,,,
Ob7Ar5Wl,Reservoirs: owner and operator requirements,https://www.gov.uk/guidance/reservoirs-owner-and-operator-requirements,environmentagency,Environment Agency,eng,HTML,"How to register a reservoir, appoint a panel engineer, produce a flood plan, prepare an inspection information pack and report an incident.",17/06/2014,09/04/2021,09/04/2021,Reservoir Operators,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Reservoirs
Water Industry",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/government/publications/reservoir-emergencies-on-site-plan/reservoir-panel-engineers-responsibilities-on-site-emergency-flood-plans
https://www.gov.uk/government/publications/reservoir-emergencies-on-site-plan/reservoir-owner-and-undertaker-responsibilities-on-site-emergency-flood-plans
https://www.gov.uk/guidance/reservoir-owner-and-operator-guidance-inspection-information-pack",,,,,,
Pw6Ey0Du,Dewatering bentonite slurry waste in a bentonite recirculation plant: RPS 272,https://www.gov.uk/government/publications/dewatering-bentonite-slurry-waste-in-a-bentonite-recirculation-plant-rps-272/dewatering-bentonite-slurry-waste-in-a-bentonite-recirculation-plant-rps-272,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position on dewatering bentonite slurry waste from secant piling or the construction of retaining and containment walls.,01/02/2023,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Planning
Bentonite",Active,,,,,,https://www.gov.uk/guidance/waste-environmental-permits,,,,,,
Ce6Pq2So,Using treated asphalt waste: RPS 75,https://www.gov.uk/government/publications/using-treated-asphalt-waste,environmentagency,Environment Agency,eng,HTML,If you comply with the requirements in this regulatory position statement (RPS) you do not need an environmental permit for the final use of asphalt waste containing coal tar in construction operations.,27/03/2014,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Waste
Asphalt
Recycling",Active,,,,,,https://www.gov.uk/guidance/waste-environmental-permits,,,,,,https://www.legislation.gov.uk/ukdsi/2010/9780111491423/
Fk7Jg4Mn,U8 waste exemption: using waste for a specified purpose,https://www.gov.uk/guidance/waste-exemption-u8-using-waste-for-a-specified-purpose,environmentagency,Environment Agency,eng,HTML,The U8 exemption allows you to use waste materials (that do not need treating) for a specific purpose to reduce the use of virgin or non-waste materials.,28/04/2014,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,"https://www.gov.uk/dispose-hazardous-waste
https://www.gov.uk/guidance/waste-exemption-s2-storing-waste-in-a-secure-place
https://www.gov.uk/guidance/waste-exemption-t4-preparatory-treatments-baling-sorting-shredding-etc
https://www.gov.uk/guidance/waste-exemption-t6-treating-waste-wood-and-waste-plant-matter-by-chipping-shredding-cutting-or-pulverising
https://www.gov.uk/guidance/waste-exemption-t12-manually-treating-waste
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Ve2Ze2Ql,Check if you need a licence to impound water,https://www.gov.uk/guidance/check-if-you-need-a-licence-to-impound-water,environmentagency,Environment Agency,eng,HTML,"If you impound water, or plan to, an impounding license may be needed.",31/03/2022,09/04/2021,09/04/2021,"Water Companies
Constructions Companie",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water
Impounding Water
Drought",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/check-if-you-need-a-licence-to-abstract-water
https://www.gov.uk/guidance/get-advice-before-you-apply-for-a-water-abstraction-or-impounding-licence
https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence",,,,,,
Bi2Mc4Jv,Reservoir owner and operator guidance: inspection information pack,https://www.gov.uk/guidance/reservoir-owner-and-operator-guidance-inspection-information-pack,environmentagency,Environment Agency,eng,HTML,Owners and operators of high risk reservoirs should create and maintain an inspection information pack for their reservoir.,06/07/2021,09/04/2021,09/04/2021,Reservoir Operators,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Reservoirs
Water Industry",,,,,,,"https://www.gov.uk/government/publications/reservoir-emergencies-on-site-plan/reservoir-owner-and-undertaker-responsibilities-on-site-emergency-flood-plans
https://www.hse.gov.uk/construction/cdm/2015/index.htm",,,,,,https://www.legislation.gov.uk/ukpga/1975/23
Xs1Nq2Gk,T8 waste exemption: mechanically treating end-of-life tyres,https://www.gov.uk/guidance/waste-exemption-t8-mechanically-treating-end-of-life-tyres,environmentagency,Environment Agency,eng,HTML,"The T8 exemption allows you to treat small amounts of waste end-of-life tyres for recovery by baling, shredding, peeling, shaving or granulating.",28/04/2014,09/04/2021,09/04/2021,"Car Garages
Construction Companies
Scrapyards",GB-ENG,"46770
45200
45310
45320",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Tyres",Active,,,,,,"https://www.gov.uk/government/publications/low-risk-waste-positions-tyres-rubber-and-plastic/storing-and-treating-rubber-encased-metal-wire-from-the-manufacture-of-new-tyres-for-recovery-lrwp-18
https://www.gov.uk/government/publications/low-risk-waste-positions-tyres-rubber-and-plastic/sorting-waste-tyres-under-a-t8-waste-exemption-lrwp-72
https://www.gov.uk/guidance/waste-exemption-u2-use-of-baled-end-of-life-tyres-in-construction
https://www.gov.uk/guidance/waste-exemption-u8-using-waste-for-a-specified-purpose
https://www.gov.uk/guidance/waste-exemption-u9-using-waste-to-manufacture-finished-goods
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/guidance/waste-environmental-permits",,,,,,https://www.legislation.gov.uk/uksi/2008/2852
Es8Ik1Qq,Safe passage for eels,https://www.gov.uk/guidance/safe-passage-for-eels,environmentagency,Environment Agency,eng,HTML,When you may need to fit an eel pass or screen to a water structure and what to submit if applying for a new licence or environmental permit.,22/06/2017,09/04/2021,09/04/2021,"Construction Companies
Waterways Operators
Water Companies
Reservoir Operators",GB-ENG,"42910
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Impact
Waterways
Eels",Active,,,,,,https://www.gov.uk/guidance/flood-risk-activities-environmental-permits,,,,,,
Na7Hc1Mt,"Storing silage, slurry and agricultural fuel oil",https://www.gov.uk/guidance/storing-silage-slurry-and-agricultural-fuel-oil,environmentagency,Environment Agency,eng,HTML,"You must follow these rules if you store silage, slurry or agricultural fuel oil.

You need to know the general rules that apply if you store any of the 3 substances, as well as specific rules for storing and handling each one.",26/03/2015,09/04/2021,09/04/2021,"Farmers
Constrction Companies",GB-ENG,"01500
01621
01629
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Farming
Silage
Acricultural Waste",Active,,,,,,"https://www.gov.uk/guidance/storing-organic-manures-in-nitrate-vulnerable-zones
https://landingpage.bsigroup.com/LandingPage/Series?UPI=BS%205502
https://knowledge.bsigroup.com/products/code-of-practice-for-design-of-concrete-structures-for-retaining-aqueous-liquids?version=standard
https://knowledge.bsigroup.com/products/structural-use-of-concrete-code-of-practice-for-design-and-construction?version=standard
https://knowledge.bsigroup.com/products/bituminous-mixtures-material-specifications-hot-rolled-asphalt-1?version=standard
https://knowledge.bsigroup.com/products/buildings-and-structures-for-agriculture-code-of-practice-for-design-construction-and-loading?version=standard
https://www.gov.uk/guidance/using-a-mechanical-slurry-separator-to-manage-your-slurry
https://knowledge.bsigroup.com/products/buildings-and-structures-for-agriculture-code-of-practice-for-design-construction-and-use-of-storage-tanks-and-reception-pits-for-livestock-slurry?version=standard
https://knowledge.bsigroup.com/products/methods-of-test-for-soils-for-civil-engineering-purposes-consolidation-and-permeability-tests-in-hydraulic-cells-and-with-pore-pressure-measurement?version=standard
https://knowledge.bsigroup.com/products/eurocode-7-geotechnical-design-ground-investigation-and-testing?version=standard
https://www.gov.uk/guidance/storing-oil-at-a-home-or-business",,,,,,
Kb7Hw3Kv,D1 waste exemption: depositing waste from dredging inland waters,https://www.gov.uk/guidance/d1-waste-exemption-depositing-waste-from-dredging-inland-waters,environmentagency,Environment Agency,eng,HTML,The D1 exemption allows you to deposit dredging spoil on the banks of the water it was dredged from and treat it by screening and removing water.,12/09/2019,09/04/2021,09/04/2021,"Construction Companies
Waterways Operators",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waterways
Dredging
Inland Waters",Active,,,,,,"https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/government/publications/the-meaning-of-place-under-the-new-waste-exemption-system
https://www.gov.uk/guidance/depositing-dredged-waste-on-land
https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/waste-exemptions-using-waste
https://www.gov.uk/guidance/waste-exemption-u13-spreading-plant-matter-to-provide-benefits
https://www.gov.uk/guidance/waste-exemption-u10-spreading-waste-to-benefit-agricultural-land
",,,,,,https://www.legislation.gov.uk/uksi/2010/639
Ea8Ea3Fh,Preparing a flood risk assessment: standing advice,https://www.gov.uk/guidance/flood-risk-assessment-standing-advice,environmentagency,Environment Agency,eng,HTML,Find out if you need to follow standing advice when completing a flood risk assessment and what to do.,01/04/2012,09/04/2021,09/04/2021,"Construction Companies
Local Authorities",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Environmental Impacts
Planning",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-assessment-local-planning-authorities
https://www.gov.uk/guidance/flood-risk-assessment-for-planning-applications
https://www.gov.uk/guidance/flood-risk-and-coastal-change#site-specific-flood-risk-assessment-checklist
https://www.gov.uk/government/publications/sustainable-drainage-systems-non-statutory-technical-standards
https://www.gov.uk/guidance/flood-risk-assessments-climate-change-allowances
https://knowledge.bsigroup.com/products/flood-resistance-products-building-products-specification-1?version=standard
https://knowledge.bsigroup.com/products/flood-resistant-and-resilient-construction-guide-to-improving-the-flood-performance-of-buildings?version=standard
https://knowledge.bsigroup.com/products/protection-of-below-ground-structures-against-water-ingress-code-of-practice?version=standard
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/regional-flood-defence-and-land-drainage-byelaws-activities-and-locations-covered-by-the-byelaws
https://www.gov.uk/guidance/owning-a-watercourse
https://www.gov.uk/guidance/using-modelling-for-flood-risk-assessments
https://www.gov.uk/government/publications/electrical-safety-approved-document-p
https://historicengland.org.uk/advice/your-home/flooding-and-older-homes/being-prepared-for-flooding/
https://www.gov.uk/government/publications/drainage-and-waste-disposal-approved-document-h",,,,,,
Jv7Ed6Bn,"Flood risk assessment: flood zones 1, 2, 3 and 3b",https://www.gov.uk/guidance/flood-risk-assessment-flood-zones-1-2-3-and-3b,environmentagency,Environment Agency,eng,HTML,How to carry out a flood risk assessment so that you can complete your planning application,24/05/2024,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Environmental Impacts",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-assessment-for-planning-applications
https://www.gov.uk/guidance/flood-risk-assessment-local-planning-authorities
https://www.gov.uk/guidance/flood-risk-and-coastal-change
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/regional-flood-defence-and-land-drainage-byelaws-activities-and-locations-covered-by-the-byelaws
https://www.gov.uk/guidance/owning-a-watercourse
https://www.gov.uk/guidance/flood-risk-assessments-climate-change-allowances
https://www.gov.uk/guidance/using-modelling-for-flood-risk-assessments
https://knowledge.bsigroup.com/products/flood-resistance-products-building-products-specification-1?version=standard
https://knowledge.bsigroup.com/products/protection-of-below-ground-structures-against-water-ingress-code-of-practice?version=standard
https://historicengland.org.uk/advice/your-home/flooding-and-older-homes/being-prepared-for-flooding/
https://www.gov.uk/government/publications/fire-safety-approved-document-b
https://www.gov.uk/government/publications/drainage-and-waste-disposal-approved-document-h
https://www.gov.uk/government/publications/planning-and-marine-licence-advice-standard-terms-for-our-charges",,,,,,https://www.legislation.gov.uk/ukpga/2010/29/section/19
Pe1Ni3Vb,Oil storage regulations for businesses,https://www.gov.uk/guidance/storing-oil-at-a-home-or-business,environmentagency,Environment Agency,eng,HTML,"How to store oil, design standards for tanks and containers, where to locate and how to protect them, and capacity of bunds and drip trays.",06/05/2015,09/04/2021,09/04/2021,Companies storing oil or using generators/motors,GB-ENG GB-WLS,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Oil storage
Tanks
Containers
Environmental Impact",Active,,,,,,"https://www.gov.uk/guidance/storing-silage-slurry-and-agricultural-fuel-oil
https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://knowledge.bsigroup.com/products/code-of-practice-for-liquid-fuel-firing-installations-for-space-heating-and-hot-water-supply-purposes-for-domestic-buildings?version=tracked
",,,,,,
Ip1Ax5Xx,Storing organic manures in nitrate vulnerable zones,https://www.gov.uk/guidance/storing-organic-manures-in-nitrate-vulnerable-zones,environmentagency,Environment Agency,eng,HTML,How to provide enough storage and keep storage records of organic manures in a nitrate vulnerable zone (NVZ).,10/08/2015,09/04/2021,09/04/2021,Farmers,GB,"01500
01621
01629
71112",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Organic Waste
Waste Storage
Environmental Impacts",Active,,,,,,"https://www.gov.uk/guidance/using-nitrogen-fertilisers-in-nitrate-vulnerable-zones
https://www.gov.uk/guidance/storing-silage-slurry-and-agricultural-fuel-oil
https://www.gov.uk/guidance/using-a-mechanical-slurry-separator-to-manage-your-slurry",,,,,,
Ix4Si6Ll,Manage water on land: guidance for land managers,https://www.gov.uk/guidance/manage-water-on-land-guidance-for-land-managers,environmentagency,Environment Agency,eng,HTML,"How to manage water use, levels, drainage and irrigation, and avoid pollution from waste water and sheep dip.",19/02/2015,09/04/2021,09/04/2021,"Farmers
Land Managers
Construction Companies",GB,"01500
01621
01630",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Use
Drainage
Irrigation
Pollution",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/guidance/cutting-vegetation-in-inland-freshwater-environmental-permit-exemption
https://www.gov.uk/guidance/owning-a-watercourse#get-permission-for-works-on-or-near-a-watercourse
https://www.gov.uk/guidance/waste-exemption-t32-treatment-of-waste-in-a-biobed-or-biofilter
https://www.gov.uk/guidance/sheep-dip-groundwater-protection-code
https://www.gov.uk/government/publications/environment-agency-enforcement-and-sanctions-statement",,,,,,
Ur1Bg9Os,Qualifications to service equipment containing ozone-depleting substances,https://www.gov.uk/guidance/qualifications-to-service-equipment-containing-ozone-depleting-substances-hcfcs,environmentagency,Environment Agency,eng,HTML,You must have individual qualifications to work with hydrochlorofluorocarbons (HCFCs) - a type of ozone-depleting substance (ODS).,16/10/2019,09/04/2021,09/04/2021,"Electrical Engineers
Electricians",GB,"33140
27510",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"HCFCs
Appliances
Environmental Impacts",Active,,,,,,,,,,,,
Le5Jj9Ez,Qualifications to work with F gas,https://www.gov.uk/guidance/qualifications-required-to-work-on-equipment-containing-f-gas,environmentagency,Environment Agency,eng,HTML,The qualifications you need to work with fluorinated gas (F gas) and the organisations that offer them.,31/12/2014,09/04/2021,09/04/2021,"Electrical Engineers
Electricians",GB,"33140
27511",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"F gas
Appliances
Environmental Impacts",Active,,,,,,,,,,,,
Ne6Tw4Kt,Sizewell: nuclear regulation,https://www.gov.uk/guidance/sizewell-nuclear-regulation,environmentagency,Environment Agency,eng,HTML,"Environment Agency's regulation of Sizewell A, B and C and how you can find out more about environmental permits and other activities at these nuclear sites.",24/01/2020,09/04/2021,09/04/2021,Nuclear Construction Companies,GB-ENG,"42220
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Nuclear power stations
Sizewell
Permits",Active,,,,,,"https://www.gov.uk/guidance/nuclear-sites-environmental-regulation
https://www.gov.uk/guidance/monitoring-radioactivity",,,,,,
Ei6Bd9Ux,"T6 waste exemption: treating waste wood and waste plant matter by chipping, shredding, cutting or pulverising",https://www.gov.uk/guidance/waste-exemption-t6-treating-waste-wood-and-waste-plant-matter-by-chipping-shredding-cutting-or-pulverising,environmentagency,Environment Agency,eng,HTML,"The T6 exemption allows you to chip, shred, cut or pulverise waste wood and plant matter to make it easier to store and transport, or to convert it for use.",28/04/2014,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Wood",Active,,,,,,"https://www.gov.uk/guidance/waste-exemption-t23-aerobic-composting-and-associated-prior-treatment
https://www.gov.uk/guidance/waste-exemption-t24-anaerobic-digestion-at-premises-used-for-agriculture-and-burning-resulting-biogas
https://www.gov.uk/guidance/waste-exemption-t25-anaerobic-digestion-at-premises-not-used-for-agriculture-and-burning-resulting-biogas
https://www.gov.uk/guidance/waste-exemption-u9-using-waste-to-manufacture-finished-goods
https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction
https://www.gov.uk/guidance/waste-exemption-u4-burning-of-waste-as-a-fuel-in-a-small-appliance
https://www.gov.uk/guidance/waste-exemption-u8-using-waste-for-a-specified-purpose
https://www.gov.uk/guidance/waste-exemption-u12-using-mulch
https://www.gov.uk/guidance/waste-exemption-u13-spreading-plant-matter-to-provide-benefits
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/guidance/waste-environmental-permits",,,,,,
Wb0Ib5Bx,Noise impact assessments involving calculations or modelling,https://www.gov.uk/guidance/noise-impact-assessments-involving-calculations-or-modelling,environmentagency,Environment Agency,eng,HTML,Information you must submit to the Environment Agency in a noise impact assessment that uses computer modelling or spreadsheet calculations.,23/10/2018,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38118",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Noise Pollution
Environmental Impact",Active,,,,,,,,,,,,
Hq1Nl1Ej,Develop a management system: environmental permits for flood risk activity,https://www.gov.uk/guidance/develop-a-management-system-flood-risk-activity-for-environmental-permits,environmentagency,Environment Agency,eng,HTML,How to develop a management system for carrying out flood risk activities under an environmental permit.,06/04/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Permits
Management",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-activity-risk-assessment-for-your-environmental-permits
https://www.gov.uk/government/publications/preparing-for-flooding-a-guide-for-regulated-sites
https://www.gov.uk/guidance/flood-risk-and-coastal-change",,,,,,
Tb5Ow4Ni,Reservoir supervising engineers: written statements and site visit reports,https://www.gov.uk/guidance/reservoir-supervising-engineers-written-statements-and-site-visit-reports,environmentagency,Environment Agency,eng,HTML,How to write a reservoir written statement and a site visit report and what information to include.,27/06/2022,09/04/2021,09/04/2021,Reservoir Operators,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Reservoirs
Water Industry",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1975/23
https://www.legislation.gov.uk/uksi/2013/1677/schedule/6
https://www.gov.uk/guidance/reservoirs-owner-and-operator-requirements"
Bj9Sl0Va,Flood risk activity risk assessment for your environmental permits,https://www.gov.uk/guidance/flood-risk-activity-risk-assessment-for-your-environmental-permits,environmentagency,Environment Agency,eng,HTML,"Check if you need to do a risk assessment, how to do a risk assessment, and how the Environment Agency can help you.",06/04/2016,09/04/2021,09/04/2021,Constructions Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Permits",Active,,,,,,"https://www.gov.uk/guidance/develop-a-management-system-flood-risk-activity-for-environmental-permits
https://www.gov.uk/guidance/flood-and-sea-defences-when-maintenance-stops
https://www.gov.uk/government/publications/water-framework-directive-how-to-assess-the-risk-of-your-activity
https://www.gov.uk/guidance/flood-risk-assessment-for-planning-applications",,,,,,
Mp9By4Nh,Nuclear sites: environmental regulation,https://www.gov.uk/guidance/nuclear-sites-environmental-regulation,environmentagency,Environment Agency,eng,HTML,How the Environment Agency regulates the different types of nuclear sites and protects people and the environment.,24/05/2021,09/04/2021,09/04/2021,Nuclear Construction Companies,GB-ENG,"42220
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Nuclear power stations
Permits",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/guidance/nuclear-sites-rsr-environmental-permits
https://www.gov.uk/guidance/access-the-public-register-for-environmental-information
https://www.gov.uk/guidance/new-nuclear-power-stations-assessing-reactor-designs
https://www.gov.uk/guidance/sizewell-nuclear-regulation
https://www.gov.uk/guidance/hinkley-point-nuclear-regulation
https://www.gov.uk/government/publications/new-nuclear-power-plants-generic-design-assessment-guidance-for-requesting-parties/new-nuclear-power-plants-generic-design-assessment-guidance-for-requesting-parties
https://www.gov.uk/government/publications/decommissioning-of-nuclear-sites-and-release-from-regulationhttps://www.gov.uk/guidance/regulating-the-geological-disposal-of-radioactive-waste-environmental-protection
https://www.gov.uk/guidance/monitoring-radioactivity
https://www.gov.uk/guidance/sellafield-nuclear-regulation",,,,,,
Ti3Ah7We,S2 waste exemption: storing waste in a secure place,https://www.gov.uk/guidance/s2-waste-exemption-storing-waste-in-a-secure-place,environmentagency,Environment Agency,eng,HTML,"The S2 waste exemption allows you to store specific waste at a secure intermediate site, separate to where the waste was produced, before transportation to another site for recovery.",12/09/2019,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Waste Storage",Active,,,,,,"https://www.gov.uk/guidance/waste-exemptions-treating-waste
https://www.gov.uk/guidance/waste-exemption-t4-preparatory-treatments-baling-sorting-shredding-etc
https://www.gov.uk/guidance/waste-exemption-t11-repairing-or-refurbishing-waste-electrical-and-electronic-equipment-weee
https://www.gov.uk/government/collections/waste-exemptions-using-waste
https://www.gov.uk/guidance/waste-exemption-t2-recovering-textiles
https://www.gov.uk/guidance/waste-exemptions-storing-waste
https://www.gov.uk/guidance/waste-environmental-permits
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Sd1Tl7Cq,T10 waste exemption: sorting mixed waste,https://www.gov.uk/guidance/waste-exemption-t10-sorting-mixed-waste,environmentagency,Environment Agency,eng,HTML,"The T10 exemption allows small organisations, such as charities, to sort recyclable waste so that it can be recovered.",28/04/2014,09/04/2021,09/04/2021,"Small organisations
Charities",GB-ENG,"88990
87900",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,"https://www.gov.uk/guidance/waste-exemption-u3-construction-of-entertainment-or-educational-installations
https://www.gov.uk/guidance/waste-exemption-u9-using-waste-to-manufacture-finished-goods
https://www.gov.uk/guidance/waste-exemptions-treating-waste
https://www.gov.uk/guidance/waste-exemption-t2-recovering-textiles
https://www.gov.uk/guidance/waste-exemption-t4-preparatory-treatments-baling-sorting-shredding-etc
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permitshttps://www.gov.uk/guidance/waste-environmental-permits",,,,,,
Se4If3Ck,Non-impounding reservoir panel engineers: contact details,https://www.gov.uk/guidance/non-impounding-reservoir-panel-engineers-contact-details,environmentagency,Environment Agency,eng,HTML,Appoint a panel engineer for your reservoir.,21/12/2023,09/04/2021,09/04/2021,Reservoir Operators,GB-ENG GB-WLS,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Reservoirs
Engineers",Active,,,,,,,,,,,,
Gr0Fi7Pa,Specified generator: when you need a permit,https://www.gov.uk/guidance/specified-generator-when-you-need-a-permit,environmentagency,Environment Agency,eng,HTML,Find out if and by when you need to apply for a specified generator environmental permit to meet air quality requirements.,15/07/2019,09/04/2021,09/04/2021,"Construction Companies
Generator Users",GB-ENG GB-WLS,"27110
25300
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Generators
Permits
Pollution",Active,,,,,,"https://www.gov.uk/guidance/medium-combustion-plant-when-you-need-a-permit
https://www.gov.uk/government/publications/operating-a-schedule-25b-tranche-b-specified-generator-for-research-and-development-rps-220
https://www.gov.uk/guidance/specified-generator-comply-with-permit-conditions
https://www.gov.uk/guidance/part-b-activities-combustion-and-incineration-permits",,,,,,
Jb9Fs7Di,Quality protocol: pulverised fuel ash (PFA) and furnace bottom ash (FBA),https://www.gov.uk/government/publications/quality-protocol-pulverised-fuel-ash-pfa-and-furnace-bottom-ash-fba,environmentagency,Environment Agency,eng,HTML,End of waste criteria for the production of PFA and FBA for use in bound and grout applications in specified construction and manufacturing uses.,01/10/2010,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Ash
Waste
Recycling",Active,,,,,,,,,,,,
Vp5Jo5Ln,Check if you need a licence to abstract water,https://www.gov.uk/guidance/check-if-you-need-a-licence-to-abstract-water,environmentagency,Environment Agency,eng,HTML,"If you abstract water or plan to, you may need to apply for an abstraction licence.",31/03/2022,09/04/2021,09/04/2021,"Construction Companies
Water Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38117
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water
Abstraction
Environmental Resources",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-a-licence-to-impound-water

https://www.gov.uk/government/publications/passive-dewatering-regulatory-position-statement/passive-dewatering-regulatory-position-statement
https://www.gov.uk/government/publications/rainwater-harvesting-regulatory-position-statement/rainwater-harvesting-regulatory-position-statement
https://www.gov.uk/guidance/get-advice-before-you-apply-for-a-water-abstraction-or-impounding-licence
https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence",,,,,,
Lq2Kp0Ep,T11 waste exemption: repairing or refurbishing waste electrical and electronic equipment (WEEE),https://www.gov.uk/guidance/waste-exemption-t11-repairing-or-refurbishing-waste-electrical-and-electronic-equipment-weee,environmentagency,Environment Agency,eng,HTML,"The T11 exemption allows you to repair, refurbish or dismantle various types of WEEE so that the whole WEEE item or any parts can be reused for their original purpose or recovered.",28/04/2014,09/04/2021,09/04/2021,"Electronics Companies
Construction Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
26400
26110
27110
33140
27900
27520
27510
27400",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Electronics",Active,,,,,,"https://www.gov.uk/guidance/waste-exemption-s2-storing-waste-in-a-secure-place
https://www.gov.uk/guidance/waste-environmental-permits",,,,,,
Pm2Bk0Cq,Waste exemption: NWFD 4 temporary storage at a collection point,https://www.gov.uk/guidance/waste-exemption-nwfd-4-temporary-storage-at-a-collection-point,environmentagency,Environment Agency,eng,HTML,This exemption allows you to temporarily store waste at a collection point before recovering or disposing of the waste elsewhere.,28/04/2014,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Waste Storage
Recycling",Active,,,,,,,,,,,,
Kr3Ju5Ir,Check if your material is waste,https://www.gov.uk/guidance/check-if-your-material-is-waste,environmentagency,Environment Agency,eng,HTML,"When a material is waste, is a by-product or meets 'end of waste' status.",31/08/2021,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38120",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,https://www.gov.uk/guidance/request-a-resource-framework-to-show-when-a-material-has-ceased-to-be-waste,,,,,,https://www.legislation.gov.uk/eudr/2008/98
Fk5Ea0Tc,"Register, renew or change waste exemptions",https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits,environmentagency,Environment Agency,eng,HTML,When your waste operation does not need a permit but you may need to register.,01/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/guidance/waste-exemption-t11-repairing-or-refurbishing-waste-electrical-and-electronic-equipment-weee
https://www.gov.uk/guidance/waste-exemption-nwfd-2-temporary-storage-at-the-place-of-production--2
https://www.gov.uk/guidance/waste-exemption-nwfd-3-temporary-storage-of-waste-at-a-place-controlled-by-the-producer
https://www.gov.uk/guidance/waste-exemption-nwfd-4-temporary-storage-at-a-collection-point",,,,,,
Fw8Ow7Al,Reservoir owner and operator guidance: spillways,https://www.gov.uk/guidance/reservoir-owner-and-operator-guidance-spillways,environmentagency,Environment Agency,eng,HTML,"How to design, inspect, monitor and maintain impounding reservoir spillways so they are safe.",27/06/2022,09/04/2021,09/04/2021,Reservoir Operators,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Reservoirs
Spillways",Active,,,,,,"https://www.gov.uk/guidance/reservoirs-owner-and-operator-requirements
https://www.hse.gov.uk/construction/cdm/2015/index.htm
https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/guidance/reservoir-inspecting-engineers-safety-inspection-of-reservoirs",,,,,,
Ra1Xv6Bs,Emergency backup diesel engines on installations: best available techniques (BAT),https://www.gov.uk/guidance/emergency-backup-diesel-engines-on-installations-best-available-techniques-bat,environmentagency,Environment Agency,eng,HTML,"BAT for diesel engines on an installation that are classed as new medium combustion plant, operating up to 500 hours a year that are exempt from emission limit values (ELVs).",21/08/2023,09/04/2021,09/04/2021,"Generator Users
Construction Companies",GB-ENG,"27110
25300
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Diesel Engines
Emergency backup
Pollution
Environmental Impact",Active,,,,,,,,,,,,
Cl8Gx4Ti,Apply to build a new hydropower scheme,https://www.gov.uk/guidance/new-hydropower-scheme-apply-to-build-one,environmentagency,Environment Agency,eng,HTML,"The licences and permits you need, the documents you must prepare, and how to apply to build a hydropower scheme.",10/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Hydropower
Permits
Clean Energy",Active,,,,,,"https://www.gov.uk/guidance/fish-pass-approval
https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/get-advice-before-you-apply-for-a-water-abstraction-or-impounding-licence
https://www.gov.uk/government/publications/water-resources-licences-when-and-how-you-are-charged
https://www.gov.uk/guidance/comply-with-your-water-abstraction-or-impounding-licence",,,,,,
Zq4Ek6Nh,T9 waste exemption: recovering scrap metal,https://www.gov.uk/guidance/waste-exemption-t9-recovering-scrap-metal,environmentagency,Environment Agency,eng,HTML,"The T9 exemption allows you to treat scrap metal for handling or recovery by sorting, grading, shearing by manual feed, baling, crushing or cutting with handheld equipment.",28/04/2014,09/04/2021,09/04/2021,"Construction Companies
Scrapyards",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38122
38320
46770",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits",Active,,,,,,"https://www.gov.uk/guidance/waste-exemption-u16-using-depolluted-end-of-life-vehicles-for-parts
https://www.gov.uk/guidance/s2-waste-exemption-storing-waste-in-a-secure-place
https://www.gov.uk/guidance/waste-exemption-u3-construction-of-entertainment-or-educational-installations
https://www.gov.uk/guidance/waste-exemption-u9-using-waste-to-manufacture-finished-goods
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Nl7Qn2Nh,T32 waste exemption: treatment of waste in a biobed or biofilter,https://www.gov.uk/guidance/waste-exemption-t32-treatment-of-waste-in-a-biobed-or-biofilter,environmentagency,Environment Agency,eng,HTML,The T32 exemption allows you to treat non-hazardous pesticide washings in a biobed or biofilter.,28/04/2014,09/04/2021,09/04/2021,Farmers,GB-ENG,"01500
01621
01629",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits
Pesticides",Active,,,,,,"https://www.gov.uk/guidance/groundwater-source-protection-zones-spzs
https://www.gov.uk/guidance/waste-exemption-t29-treatment-of-non-hazardous-pesticide-washings-by-carbon-filtration-for-disposal
https://www.gov.uk/guidance/waste-exemption-u10-spreading-waste-to-benefit-agricultural-land
https://www.gov.uk/guidance/waste-exemption-u11-spreading-waste-to-benefit-non-agricultural-land
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Ae8Es9Np,D8 waste exemption: burning waste at a port under a Plant Health Notice,https://www.gov.uk/guidance/d8-waste-exemption-burning-waste-at-a-port-under-a-plant-health-notice,environmentagency,Environment Agency,eng,HTML,"The D8 exemption allows you to burn plant tissue waste, wood packaging and packing material waste at a port when a Plant Health Notice has been issued, to prevent the spread of plant diseases.",12/09/2019,09/04/2021,09/04/2021,Port Authorities,GB-ENG,"50200
50400
52101",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Plant Waste
Ports
Plant Diseases",Active,,,,,,https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits,,,,,,"https://www.legislation.gov.uk/uksi/2005/2530
https://www.legislation.gov.uk/wsi/2006/1344/made
https://www.legislation.gov.uk/uksi/2005/2517
https://www.legislation.gov.uk/wsi/2006/1643
https://www.legislation.gov.uk/ukpga/1979/2"
Ob2Gs7Og,Send environmental permit application information in stages,https://www.gov.uk/guidance/send-environmental-permit-application-information-in-stages,environmentagency,Environment Agency,eng,HTML,How to request a longer timetable for the Environment Agency to assess if your proposal can be 'duly made'.,21/02/2024,09/04/2021,09/04/2021,"Permit Applicants
Construction Companies",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38122
38320
46770
01500
01621
01629
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits",Active,,,,,,https://www.gov.uk/government/publications/environmental-permits-and-abstraction-licences-tables-of-charges,,,,,,
Ks5Rr3Xz,Water Framework Directive assessment: estuarine and coastal waters,https://www.gov.uk/guidance/water-framework-directive-assessment-estuarine-and-coastal-waters,environmentagency,Environment Agency,eng,HTML,How to assess the impact of your activity in estuarine (transitional) and coastal waters for the Water Framework Directive (WFD). The guidance is called Clearing the Waters for All.,15/12/2016,09/04/2021,09/04/2021,Construction Companies,GB,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Quality
Environmental Impact",Active,,,,,,"https://www.gov.uk/government/publications/self-service-marine-licensing
https://www.gov.uk/guidance/fast-track-and-accelerated-licensing
https://www.gov.uk/government/publications/list-of-chemicals-for-water-framework-directive-assessments
https://www.gov.uk/guidance/surface-water-pollution-risk-assessment-for-your-environmental-permit",,,,,,
Pt9Ej9Xt,Open loop heat pump systems: apply to install one,https://www.gov.uk/guidance/open-loop-heat-pump-systems-permits-consents-and-licences,environmentagency,Environment Agency,eng,HTML,"The environmental permit, consent and licence you may need before you install a ground source or surface water source heating or cooling system.",01/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Pumps
Water Quality
Environmental Impact
Ground Water",Active,,,,,,"https://www.gov.uk/guidance/closed-loop-ground-source-heating-and-cooling-systems-when-you-need-a-permit
https://www.gov.uk/guidance/deep-geothermal-energy-regulation
https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence
https://www.gov.uk/government/publications/water-resources-licences-when-and-how-you-are-charged

https://www.gov.uk/guidance/groundwater-source-protection-zones-spzs
https://www.gov.uk/government/publications/standard-rules-sr2010-number-2-discharge-to-surface-water
https://www.gov.uk/guidance/get-advice-before-you-apply-for-an-environmental-permit
https://www.gov.uk/guidance/discharges-to-surface-water-and-groundwater-environmental-permits
https://www.gov.uk/guidance/control-and-monitor-emissions-for-your-environmental-permit
https://www.gov.uk/guidance/develop-a-management-system-environmental-permits
https://www.gov.uk/guidance/get-advice-before-you-apply-for-a-water-abstraction-or-impounding-licence
https://www.gov.uk/guidance/get-advice-before-you-apply-for-an-environmental-permit
https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/how-youll-be-regulated-environmental-permits
https://www.gov.uk/guidance/change-a-water-abstraction-or-impoundment-licence
https://www.gov.uk/guidance/change-transfer-or-cancel-your-environmental-permit",,,,,,
Zu5Yt1Gc,U16 waste exemption: using depolluted end-of-life vehicles for parts,https://www.gov.uk/guidance/waste-exemption-u16-using-depolluted-end-of-life-vehicles-for-parts,environmentagency,Environment Agency,eng,HTML,The U16 exemption allows you to reuse the parts from depolluted end-of-life vehicles in other vehicles.,28/04/2014,09/04/2021,09/04/2021,"Construction Companies
Scrapyards",GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38122
38320
46770",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Vehicles
Scrap
Recycling
Waste",Active,,,,,,"https://www.gov.uk/guidance/waste-exemption-t9-recovering-scrap-metal
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits",,,,,,
Tm4Km8Md,Depositing dredged waste on land,https://www.gov.uk/guidance/depositing-dredged-waste-on-land,environmentagency,Environment Agency,eng,HTML,This guide is for anyone who dredges inland waterways and wants to deposit the dredged waste on land. It does not apply to hydrodynamic dredging or waste disposal at sea.,21/04/2021,09/04/2021,09/04/2021,"Construction Companies
Water Companies
Dredging Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Dredging
Waterways
River Construction",Active,,,,,,"https://www.gov.uk/guidance/do-i-need-a-marine-licence
https://www.gov.uk/guidance/d1-waste-exemption-depositing-waste-from-dredging-inland-waters
https://www.gov.uk/guidance/u1-waste-exemption-use-of-waste-in-construction
https://www.gov.uk/guidance/waste-exemption-u10-spreading-waste-to-benefit-agricultural-land
https://www.gov.uk/guidance/waste-exemption-u11-spreading-waste-to-benefit-non-agricultural-land
https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/government/publications/the-meaning-of-place-under-the-new-waste-exemption-system
https://www.gov.uk/guidance/waste-environmental-permits#check-if-you-can-get-a-standard-rules-permit
https://www.gov.uk/guidance/hazardous-waste-segregation-and-mixing",,,,,,https://www.legislation.gov.uk/uksi/2016/1154/schedule/3/made
Tr4Hd3Wh,"Get environmental advice on neighbourhood plans, development orders and community right to build orders",https://www.gov.uk/guidance/consulting-on-neighbourhood-plans-and-development-orders,environmentagency,Environment Agency,eng,HTML,"Find out which environmental agencies you need to consult about your neighbourhood plan, neighbourhood development order or CRTBO.",29/03/2015,09/04/2021,09/04/2021,"Town Councils
Parish Councils
Community Organizations
Neighbourhood Forums",GB-ENG,"41201
41202",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Planning
Neighbourhood Plans
Right to Build Orders",Active,,,,,,"https://www.gov.uk/guidance/strategic-environmental-assessment-and-sustainability-appraisal
https://www.gov.uk/guidance/neighbourhood-planning--2
https://www.gov.uk/guidance/construction-near-protected-areas-and-wildlife
https://www.gov.uk/guidance/natural-environment
https://www.gov.uk/guidance/environmental-impact-assessment
https://www.gov.uk/guidance/protected-species-how-to-review-planning-applications
https://www.gov.uk/guidance/ancient-woodland-ancient-trees-and-veteran-trees-advice-for-making-planning-decisions
https://www.gov.uk/guidance/flood-risk-and-coastal-change",,,,,,
Io4Kh7Iq,Control and monitor emissions for your environmental permit,https://www.gov.uk/guidance/control-and-monitor-emissions-for-your-environmental-permit,environmentagency,Environment Agency,eng,HTML,How you must control and monitor emissions from your activities that may cause pollution.,01/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits
Pollution",Active,,,,,,"https://www.gov.uk/guidance/risk-assessments-for-your-environmental-permit
https://www.gov.uk/guidance/develop-a-management-system-environmental-permits
Site-specific
quality
numeric
permit
limits:
discharges
to
surface
water
and
groundwater
https://www.gov.uk/government/publications/site-specific-quality-numeric-permit-limits-discharges-to-surface-water-and-groundwater
https://www.gov.uk/guidance/risk-assessments-for-your-environmental-permit
https://www.gov.uk/government/publications/groundwater-source-protection-zones
https://www.gov.uk/government/publications/environmental-permitting-h4-odour-management
https://www.gov.uk/government/publications/water-companies-operator-self-monitoring-osm-environmental-permits
https://www.gov.uk/government/publications/waste-water-treatment-works-treatment-monitoring-and-compliance-limits
https://www.gov.uk/government/publications/m9-environmental-monitoring-of-bioaerosols-at-regulated-facilities",,,,,,
Sd2Uc3Mj,Apply for a water abstraction or impounding licence,https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence,environmentagency,Environment Agency,eng,HTML,How to apply to the Environment Agency for a water abstraction or impounding licence.,08/05/2014,09/04/2021,09/04/2021,"Construction Companies
Water Companies
Dredging Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Impounding
Water Abstraction
Permits
Licenses",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-a-licence-to-abstract-water
https://www.gov.uk/guidance/check-if-you-need-a-licence-to-impound-water
https://www.gov.uk/guidance/trade-water-abstraction-rights
https://www.gov.uk/government/publications/abstract-or-impound-water-hydrological-information
https://www.gov.uk/government/publications/apply-for-consent-to-investigate-a-groundwater-source
https://www.gov.uk/guidance/get-advice-before-you-apply-for-a-water-abstraction-or-impounding-licence
https://www.gov.uk/guidance/safe-passage-for-eels
https://www.gov.uk/guidance/fish-pass-approval
https://www.gov.uk/guidance/apply-to-renew-a-water-abstraction-licence
https://www.gov.uk/government/publications/water-resources-licences-when-and-how-you-are-charged
https://www.gov.uk/guidance/new-hydropower-scheme-apply-to-build-one
https://www.gov.uk/guidance/open-loop-heat-pump-systems-permits-consents-and-licences
https://www.gov.uk/guidance/change-a-water-abstraction-or-impoundment-licence
https://www.gov.uk/guidance/comply-with-your-water-abstraction-or-impounding-licence",,,,,,
Ub4Ay9Rv,Reservoir inspecting engineers: safety inspection of reservoirs,https://www.gov.uk/guidance/reservoir-inspecting-engineers-safety-inspection-of-reservoirs,environmentagency,Environment Agency,eng,HTML,Guidance for inspecting engineers including the reporting of section 10 inspection findings.,23/02/2024,09/04/2021,09/04/2021,Reservoir Engineers,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"High Risk Reservoirs
Safety Inspection",Active,,,,,,"https://www.gov.uk/guidance/reservoir-owner-and-operator-guidance-inspection-information-pack
https://www.gov.uk/government/publications/environmental-damage-prevention-and-remediation-regulations-2009-guidance-for-england-and-wales
https://www.gov.uk/guidance/reservoir-flood-maps-when-and-how-to-use-them",,,,,,"https://www.legislation.gov.uk/ukpga/1975/23
https://www.legislation.gov.uk/uksi/2013/1677"
Ya1Dp8Pa,Groundwater risk assessment for your environmental permit,https://www.gov.uk/guidance/groundwater-risk-assessment-for-your-environmental-permit,environmentagency,Environment Agency,eng,HTML,How to carry out a groundwater risk assessment as part of an application for an environmental permit.,01/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Quality
Pollution
Permits",Active,,,,,,"https://www.gov.uk/guidance/risk-assessments-for-your-environmental-permit
https://www.gov.uk/government/publications/protect-groundwater-and-prevent-groundwater-pollution
https://www.gov.uk/government/publications/groundwater-protection-technical-guidance
https://www.gov.uk/government/publications/groundwater-activity-exclusions-from-environmental-permits",,,,,,
Ka5Vv5Hu,Cemeteries and burials: groundwater risk assessments,https://www.gov.uk/guidance/cemeteries-and-burials-groundwater-risk-assessments,environmentagency,Environment Agency,eng,HTML,How to carry out a groundwater risk assessment for human or animal burials.,14/03/2017,09/04/2021,09/04/2021,"Construction Companies
Cemetery Operators",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Cemetery
Water Quality
Pollution",Active,,,,,,"https://www.gov.uk/government/publications/protecting-groundwater-from-human-burials/protecting-groundwater-from-human-burials
https://www.gov.uk/guidance/groundwater-risk-assessment-for-your-environmental-permit
https://www.gov.uk/guidance/discharges-to-surface-water-and-groundwater-environmental-permits",,,,,,https://www.legislation.gov.uk/uksi/2016/1154
Me7Kw4Gt,Deposit for recovery operators: environmental permits,https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/waste-recovery-plans-and-deposit-for-recovery-permits,environmentagency,Environment Agency,eng,HTML,How to apply for an environmental permit to permanently deposit waste on land as a recovery activity,21/04/2021,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits",Active,,,,,,"https://www.gov.uk/government/publications/environmental-permitting-guidance-the-waste-framework-directive
https://www.gov.uk/government/publications/environmental-permits-and-abstraction-licences-tables-of-charges
https://www.gov.uk/guidance/check-if-your-material-is-waste
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/check-if-your-waste-is-suitable-for-deposit-for-recovery
https://www.gov.uk/guidance/risk-assessments-for-your-environmental-permit
https://www.gov.uk/guidance/waste-environmental-permits
https://www.gov.uk/government/publications/sr2015-no39-use-of-waste-in-a-deposit-for-recovery-operation
https://www.gov.uk/guidance/develop-a-management-system-environmental-permits
https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/waste-acceptance-procedures-for-deposit-for-recovery
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/engineering-construction-proposals-for-deposit-for-recovery
https://www.gov.uk/government/publications/landfill-epr-502-and-other-permanent-deposits-of-waste-how-to-surrender-your-environmental-permit
https://www.gov.uk/guidance/control-and-monitor-emissions-for-your-environmental-permit
https://www.gov.uk/guidance/change-transfer-or-cancel-your-environmental-permit
https://www.gov.uk/guidance/get-advice-before-you-apply-for-an-environmental-permit
https://www.gov.uk/government/publications/landspreading-apply-to-deploy-mobile-plant/landspreading-produce-a-benefit-statement",,,,,,"https://www.legislation.gov.uk/eudr/2008/98/article/3
https://www.legislation.gov.uk/uksi/2016/1154/regulation/2/made"
Oi6Lo4Vq,Closed loop ground source heating and cooling systems: exemption conditions,https://www.gov.uk/guidance/closed-loop-ground-source-heating-and-cooling-systems-exemption-conditions,environmentagency,Environment Agency,eng,HTML,Check if you're exempt from needing an environmental permit for a new closed loop ground source heating and cooling system.,02/10/2023,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38121",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Pumps
Water Quality
Environmental Impact
Ground Water",Active,,,,,,"https://www.gov.uk/guidance/closed-loop-ground-source-heating-and-cooling-systems-when-you-need-a-permit
https://www.gov.uk/guidance/groundwater-source-protection-zones-spzs
https://www.gov.uk/guidance/closed-loop-ground-source-heating-and-cooling-systems-when-you-need-a-permit",,,,,,"https://www.legislation.gov.uk/uksi/2023/651/regulation/5/made
https://www.legislation.gov.uk/uksi/2016/1154"
Kt5Oc0Qb,Exempt flood risk activities: environmental permits,https://www.gov.uk/government/publications/environmental-permitting-regulations-exempt-flood-risk-activities/exempt-flood-risk-activities-environmental-permits,defra,Defra,eng,HTML,Check if your activity is exempt and read the conditions you'd need to meet in order to operate without a permit.,06/04/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38122",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Permits
Elevated flood risk",Active,,,,,,"https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/construction-near-protected-areas-and-wildlife
https://www.gov.uk/government/publications/dredging-as-a-flood-risk-activity-under-the-environmental-permitting-regulations",,,,,,"https://www.legislation.gov.uk/uksi/2017/407
https://www.legislation.gov.uk/ukpga/2006/16"
Ot1Xz3Me,SR2015 No 28: installing a clear span bridge,https://www.gov.uk/government/publications/sr2015-no28-installing-a-clear-span-bridge-on-a-main-river,environmentagency,Environment Agency,eng,HTML,Standard rules for installing a clear span bridge up to 8 metres span and 4.2 metres wide across a main river.,06/04/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Bridges
Engineering",Active,,,,,,,,,,,,https://www.legislation.gov.uk/uksi/2017/407
Jd9Pt3Ff,Developers: get environmental advice on your planning proposals,https://www.gov.uk/guidance/developers-get-environmental-advice-on-your-planning-proposals,environmentagency,Environment Agency,eng,HTML,"How developers can get advice on Nationally Significant Infrastructure Projects (NSIPs) and applications for planning, permission in principle and technical details consent.",29/03/2015,09/04/2021,09/04/2021,"Construction Companies
",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Infrastructure
Planning Permission",Active,,,,,,"https://www.gov.uk/government/publications/agricultural-land-assess-proposals-for-development
https://www.gov.uk/guidance/ancient-woodland-ancient-trees-and-veteran-trees-advice-for-making-planning-decisions
https://www.gov.uk/guidance/minerals
https://www.gov.uk/guidance/natural-environment
https://www.gov.uk/guidance/protected-species-how-to-review-planning-applications
https://www.gov.uk/guidance/flood-risk-assessment-local-planning-authorities
https://www.gov.uk/guidance/flood-risk-assessment-flood-zones-1-2-3-and-3b
https://www.gov.uk/guidance/river-basin-management-plans-updated-2022
https://www.hse.gov.uk/landuseplanning/about.htm
https://www.gov.uk/guidance/when-is-permission-required
https://www.gov.uk/guidance/check-if-you-need-an-environmental-permit
https://www.gov.uk/government/publications/a-coastal-concordat-for-england
https://www.gov.uk/guidance/get-advice-before-you-apply-for-an-environmental-permit
https://www.gov.uk/government/publications/developments-requiring-planning-permission-and-environmental-permits
https://www.gov.uk/guidance/environmental-impact-assessment
https://www.gov.uk/guidance/planning-act-2008-infrastructure-planning-fees-regulations-2010-cost-recovery-by-the-planning-inspectorate-and-public-authorities
https://www.gov.uk/government/publications/chargeable-services-general-terms-and-conditions
https://www.gov.uk/government/publications/planning-and-marine-licence-advice-standard-terms-for-our-charges",,,,,,
Vu0Et7Ti,General binding rules: small sewage discharge to the ground,https://www.gov.uk/guidance/general-binding-rules-small-sewage-discharge-to-the-ground,environmentagency,Environment Agency,eng,HTML,How to meet the general binding rules if your septic tank or small sewage treatment plant releases (discharges) waste water to the ground.,16/06/2015,09/04/2021,09/04/2021,"Construction Companies
Water Treatment Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Sewage
Septic Tanks
Pollution",Active,,,,,,"https://www.gov.uk/government/publications/small-sewage-discharges-in-england-the-general-binding-rules
https://www.gov.uk/guidance/general-binding-rules-small-sewage-discharge-to-a-surface-water
https://www.gov.uk/government/publications/domestic-sewage-discharges-to-surface-water-and-groundwater/domestic-sewage-discharges-to-surface-water-and-groundwater
https://www.gov.uk/guidance/comply-with-septic-tank-and-sewage-treatment-plant-permits
https://www.gov.uk/guidance/ce-marking",,,,,,
Ro0Ry1Td,Flood risk assessments: climate change allowances,https://www.gov.uk/guidance/flood-risk-assessments-climate-change-allowances,environmentagency,Environment Agency,eng,HTML,"When and how local planning authorities, developers and their agents should use climate change allowances in flood risk assessments.",19/02/2016,09/04/2021,09/04/2021,"Construction Companies
Local Planning Authorities
Developers",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Risk Assessment
Climate Change Impact",Active,,,,,,"https://www.gov.uk//guidance/flood-and-coastal-risk-projects-schemes-and-strategies-climate-change-allowances
https://www.gov.uk/guidance/flood-risk-assessment-for-planning-applications
https://www.gov.uk/guidance/local-planning-authorities-strategic-flood-risk-assessment
https://www.gov.uk/guidance/flood-risk-and-coastal-change
https://www.gov.uk/government/publications/peak-rainfall-climate-change-allowances-by-management-catchment
https://www.gov.uk/government/publications/sustainable-drainage-systems-non-statutory-technical-standards",,,,,,
Gk4Tb6Uu,Storing and treating hazardous waste cable: RPS 276,https://www.gov.uk/government/publications/storing-and-treating-hazardous-waste-cable-rps-276/storing-and-treating-hazardous-waste-cable-rps-276,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position on when you can store and treat hazardous waste cable without the correct waste codes on your permit or exemption.,31/05/2023,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Cable
Waste
Recycling",Active,,,,,,,,,,,,
Dx7Yv1Rv,Design and build your landfill site,https://www.gov.uk/guidance/landfill-operators-environmental-permits/design-and-build-your-landfill-site,environmentagency,Environment Agency,eng,HTML,The design requirements that you need to meet in your environmental permit application and how to comply with your permit.,30/01/2020,09/04/2021,09/04/2021,"Landfill Companies
Construction Companies",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38124",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Landfill
Waste
Recycling",Active,,,,,,"https://www.gov.uk/guidance/landfill-operators-environmental-permits/what-to-include-in-your-hydrogeological-risk-assessment
https://www.gov.uk/guidance/landfill-operators-environmental-permits/how-to-do-a-stability-risk-assessment-landfill-sites-for-hazardous-and-non-hazardous-waste
https://www.gov.uk/guidance/landfill-operators-environmental-permits/how-the-environment-agency-makes-decisions-on-landfill-engineering
https://www.gov.uk/guidance/landfill-operators-environmental-permits/construction-quality-assurance-cqa
https://www.gov.uk/government/publications/protect-groundwater-and-prevent-groundwater-pollution/protect-groundwater-and-prevent-groundwater-pollution
https://www.gov.uk/government/publications/earthworks-in-landfill-engineering-lfe4
https://www.gov.uk/government/publications/using-bentonite-enriched-soils-in-landfill-engineering-lfe10
https://www.gov.uk/guidance/landfill-operators-environmental-permits/manage-leachate
https://www.gov.uk/government/publications/cylinder-testing-geomembranes-and-their-protective-materials-lfe2
https://www.gov.uk/government/publications/using-non-woven-protector-geotextiles-in-landfill-engineering-lfe7
https://www.gov.uk/government/publications/using-geosynthetic-clay-liners-in-landfill-engineering-
https://www.hse.gov.uk/fireandexplosion/dsear.htm
https://www.gov.uk/guidance/landfill-operators-environmental-permits/develop-and-maintain-management-plans",,,,,,
Vk8Zk5Yq,Treating pesticide washings using lined biobeds and biofilters: RPS 140,https://www.gov.uk/government/publications/building-biobeds-in-a-groundwater-source-protection-zone-1/building-lined-biobeds-in-a-groundwater-source-protection-zone-1-rps-140,environmentagency,Environment Agency,eng,HTML,Environment Agency regulatory position on when you can treat diluted pesticide washings in lined biobeds and biofilters.,25/09/2018,09/04/2021,09/04/2021,"Users of pesticides
Farmers",GB-ENG,"01500
01621",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Pesticides
Waste
Pollution",Active,,,,,,https://www.gov.uk/guidance/waste-exemption-t32-treatment-of-waste-in-a-biobed-or-biofilter,,,,,,
Gh4Ky6Fy,New nuclear power stations: assessing reactor designs,https://www.gov.uk/guidance/new-nuclear-power-stations-assessing-reactor-designs,environmentagency,Environment Agency,eng,HTML,The Environment Agency's Generic Design Assessment (GDA) of new nuclear power station designs and how we engage with others during the process.,01/11/2019,09/04/2021,09/04/2021,Nuclear Construction Companies,GB-ENG GB-WLS,"24460
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,Nuclear Reactors,Active,,,,,,"https://www.gov.uk/government/publications/new-nuclear-power-plants-generic-design-assessment-guidance-for-requesting-parties
https://www.gov.uk/government/publications/assessment-of-candidate-nuclear-power-plant-designs",,,,,,
Hb9Zw2Vd,Water cycle studies,https://www.gov.uk/guidance/water-cycle-studies,environmentagency,Environment Agency,eng,HTML,"Find out when to prepare a water cycle study for your proposed development plan document, or development, and what to focus on.",06/01/2021,09/04/2021,09/04/2021,Local Authorities,GB-ENG,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Cycles
Planning",Active,,,,,,"https://www.gov.uk/guidance/water-supply-wastewater-and-water-quality
https://www.gov.uk/guidance/plan-making
https://www.gov.uk/government/publications/developments-requiring-planning-permission-and-environmental-permits
https://www.gov.uk/guidance/neighbourhood-planning--2
https://www.gov.uk/guidance/local-plans--2
https://www.gov.uk/guidance/environment-agency-fees-and-charges",,,,,,
Ov3Tb4Fa,Reservoir emergencies: on-site plans,https://www.gov.uk/government/publications/reservoir-emergencies-on-site-plan/reservoir-owner-and-undertaker-responsibilities-on-site-emergency-flood-plans,defra,Defra,eng,HTML,How reservoir operators should prepare on-site plans so they can respond to emergencies.,28/03/2017,09/04/2021,09/04/2021,Reservoir Operators,GB,"36000
42910",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Reservoirs",Active,,,,,,"https://www.gov.uk/guidance/reservoir-discharges-consents-permits-and-risk-assessments
https://www.gov.uk/government/publications/reservoir-emergencies-on-site-plan/reservoir-panel-engineers-responsibilities-on-site-emergency-flood-plans",,,,,,https://www.legislation.gov.uk/ukpga/1975/23
Go8Xg7Fl,"SR2010 No 10: use of waste for reclamation, restoration or improvement of land",https://www.gov.uk/government/publications/sr2010-number-10,environmentagency,Environment Agency,eng,HTML,"Standard rules to use waste for reclamation, restoration or improvement of land (existing permits only).",25/06/2012,09/04/2021,09/04/2021,Constrction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39000",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Land Improvement",Active,,,,,,,,,,,,
Dg4Eb5Lw,Using bentonite enriched soils in landfill engineering: LFE10,https://www.gov.uk/government/publications/using-bentonite-enriched-soils-in-landfill-engineering-lfe10,environmentagency,Environment Agency,eng,HTML,This document provides guidance on using bentonite enriched soils in landfill engineering.,24/06/2014,09/04/2021,09/04/2021,Landfill Operators,GB,"38110
38120
38210
38220",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Soil
Bentonite
Landfill Engineering",Active,,,,,,,,,,,,
Di4Zb5Tc,Using wetlands to improve treated effluent discharge: RPS 260,https://www.gov.uk/government/publications/using-wetlands-to-improve-treated-effluent-discharge-rps-260/using-wetlands-to-improve-treated-effluent-discharge-rps-260,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position for wetlands that receive treated final effluent discharged from water and sewerage company wastewater treatment works.,29/11/2022,09/04/2021,09/04/2021,Wetland Operators,GB-ENG,"37000
42910
36000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Wetland Discharge
Pollution",Active,,,,,,,,,,,,
Dv3Xc2Dg,"SR2010 No 9: use of waste for reclamation, restoration or improvement of land",https://www.gov.uk/government/publications/sr2010-number-9,environmentagency,Environment Agency,eng,HTML,"Standard rules for the use of waste for reclamation, restoration or improvement of land (up to 50kte).",25/06/2012,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39000",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Land Improvement
Waste
Recycling",Active,,,,,,,,,,,,https://www.legislation.gov.uk/eudr/2008/98
Qp5Jq2Sk,Hazardous waste: consignee returns guidance (England),https://www.gov.uk/guidance/hazardous-waste-returns-supplementary-guidance,environmentagency,Environment Agency,eng,HTML,How to send returns to the Environment Agency and waste producer if you receive or dispose of hazardous waste.,04/04/2014,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39000",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste Disposal
Hazardous Waste",Active,,,,,,"https://www.gov.uk/guidance/hazardous-waste-consignment-note-supplementary-guidance
https://www.gov.uk/guidance/hazardous-waste-rejected-loads-supplementary-guidance",,,,,,
Yg4Qn2Dk,Infiltration systems: groundwater risk assessments,https://www.gov.uk/guidance/infiltration-systems-groundwater-risk-assessments#risk-assessments-who-carries-it-out,environmentagency,Environment Agency,eng,HTML,How to assess the risks to groundwater for treated effluent discharges.,01/02/2016,09/04/2021,09/04/2021,"Construction Companies
Water Treatment Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Groundwater Pollution
Effluent Discharges",Active,,,,,,"https://www.gov.uk/government/publications/groundwater-protection-position-statements
https://www.gov.uk/government/publications/protect-groundwater-and-prevent-groundwater-pollution/protect-groundwater-and-prevent-groundwater-pollution
https://www.gov.uk/government/publications/values-for-groundwater-risk-assessments
https://www.gov.uk/guidance/groundwater-risk-assessment-for-your-environmental-permit",,,,,,
Hv6Dm7Zb,Valuing the carbon net impacts of FCERM projects,https://www.gov.uk/government/publications/valuing-the-carbon-net-impacts-of-fcerm-projects/valuing-the-carbon-net-impacts-of-fcerm-projects,environmentagency,Environment Agency,eng,HTML,How to include carbon in your FCERM project business case economic appraisal and the partnership funding (PF) calculator.,29/06/2022,09/04/2021,09/04/2021,"Construction Companies
Water Treatment Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38124",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Carbon
Business Case Economic Appraisal",Active,,,,,,"https://www.gov.uk/guidance/fcerm-appraisal-guidance
https://www.gov.uk/guidance/partnership-funding-for-fcerm-projects",,,,,,
Bq8Zv6Xc,SR2010 No 3: discharge to surface water,https://www.gov.uk/government/publications/sr2010-number-3-discharge-to-surface-water,environmentagency,Environment Agency,eng,HTML,Standard rules for discharges to surface water.,07/06/2013,09/04/2021,09/04/2021,"Construction Companies
Water Treatment Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38125",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Surface Water
Pollution",Active,,,,,,,,,,,,
Uw7Aw7Vn,Storing and treating rubber encased metal wire from the manufacture of new tyres for recovery: LRWP 18,https://www.gov.uk/government/publications/low-risk-waste-positions-tyres-rubber-and-plastic/storing-and-treating-rubber-encased-metal-wire-from-the-manufacture-of-new-tyres-for-recovery-lrwp-18,environmentagency,Environment Agency,eng,HTML,This low risk waste position (LRWP) applies if you store and treat rubber encased metal wire (List of Waste code 07 02 99) from the manufacture of new tyres to produce metal and tyre snippets for reuse.,20/08/2019,09/04/2021,09/04/2021,"Car Garages
Construction Companies
Scrapyards",GB-ENG,"46770
45200
45310
45320",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Tyres",Active,,,,,,,,,,,,
Po3Xl4Vn,Sorting waste tyres under a T8 waste exemption: LRWP 72,https://www.gov.uk/government/publications/low-risk-waste-positions-tyres-rubber-and-plastic/sorting-waste-tyres-under-a-t8-waste-exemption-lrwp-72,environmentagency,Environment Agency,eng,HTML,"This low risk waste position (LRWP) applies if you sort waste tyres (for example by type, size and condition) as an associated prior treatment under the T8 waste exemption: mechanically treating end-of-life tyres.",20/08/2019,09/04/2021,09/04/2021,"Car Garages
Construction Companies
Scrapyards",GB-ENG,"46770
45200
45310
45320",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Tyres",Active,,,,,,https://www.gov.uk/guidance/waste-exemption-t8-mechanically-treating-end-of-life-tyres,,,,,,
Tg0Xk5Ok,Regional flood defence and land drainage byelaws: activities and locations covered by the byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/regional-flood-defence-and-land-drainage-byelaws-activities-and-locations-covered-by-the-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39000",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage",Active,,,,,,"https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/regional-flood-defence-and-land-drainage-byelaws-activities-and-locations-covered-by-the-byelaws
https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/guidance/owning-a-watercourse
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/anglian-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/north-west-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/northumbrian-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/south-west-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/southern-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/thames-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/midlands-and-severn-trent-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/yorkshire-region-flood-defence-and-land-drainage-byelaws
https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/wessex-region-flood-defence-and-land-drainage-byelaws",,,,,,https://www.legislation.gov.uk/ukpga/1991/57
Uw0Uw5Mh,Anglian region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/anglian-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39001",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Anglian region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/58
Oh0Ub3Sd,North West region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/north-west-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39002",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
North West region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/59
Nw7Zt2Qb,Northumbrian region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/northumbrian-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39003",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Northumbrian region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/60
Tk4Um4Mw,South West region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/south-west-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39004",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
South West region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/61
Ht9Nw8Xv,Southern region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/southern-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39005",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Southern region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/62
Yy5Rk7Fr,Thames region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/thames-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39006",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/63
Im4Wx2Qs,Midlands and Severn Trent region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/midlands-and-severn-trent-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39007",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Midlands and Severn region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/64
Bg3Wd3Pn,Yorkshire region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/yorkshire-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39008",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Yorkshire region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/65
Vl0Dz4Of,Wessex region flood defence and land drainage byelaws,https://www.gov.uk/government/publications/regional-flood-defence-and-land-drainage-byelaws/wessex-region-flood-defence-and-land-drainage-byelaws,environmentagency,Environment Agency,eng,HTML,"You must follow the regional flood defence and land drainage byelaws (the byelaws) when carrying out activities:

on or near a main river
on or near a flood defence structure
in a flood plain
on or near a sea defence",29/09/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39009",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Flooding
Drainage
Wessex region",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/66
Dc8Do7Su,Aggregate from waste steel slag: quality protocol,https://www.gov.uk/government/publications/aggregate-from-waste-steel-slag-quality-protocol/aggregate-from-waste-steel-slag-quality-protocol,environmentagency,Environment Agency,eng,HTML,When aggregate made from steel slag is no longer waste.,01/04/2015,09/04/2021,09/04/2021,"Construction Companies
Steel manufacturing companies",GB-ENG GB-WLS GB-NIR,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39010
24100",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Steel slag
Aggregate",Active,,,,,,https://www.gov.uk/government/publications/waste-classification-technical-guidance,,,,,,
Va0Ns0Cp,New nuclear power plants: Generic Design Assessment guidance for Requesting Parties,https://www.gov.uk/government/publications/new-nuclear-power-plants-generic-design-assessment-guidance-for-requesting-parties/new-nuclear-power-plants-generic-design-assessment-guidance-for-requesting-parties,environmentagency,Environment Agency,eng,HTML,This guidance explains the Generic Design Assessment (GDA) process for organisations who want to submit a nuclear power plant design for assessment.,29/10/2019,09/04/2021,09/04/2021,Nuclear Construction Companies,GB,"24460
42990",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Nuclear design
Nuclear power plants",Active,,,,,,"https://www.gov.uk/government/publications/radioactive-substances-regulation-rsr-objective-and-principles
https://www.gov.uk/government/publications/incineration-of-waste-epr501-additional-guidance
https://www.gov.uk/guidance/fluorinated-gases-f-gases",,,,,,"https://www.legislation.gov.uk/ukpga/1995/25
https://www.legislation.gov.uk/uksi/2015/310
https://www.legislation.gov.uk/uksi/2015/168
https://www.legislation.gov.uk/uksi/2015/483"
Fp5Fo2Md,Passive dewatering: regulatory position statement,https://www.gov.uk/government/publications/passive-dewatering-regulatory-position-statement/passive-dewatering-regulatory-position-statement,environmentagency,Environment Agency,eng,HTML,When you do not need a water abstraction licence from the Environment Agency for passive dewatering.,10/12/2020,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39009",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Dewatering
Water Abstraction",Active,,,,,,https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence,,,,,,https://www.legislation.gov.uk/ukpga/1991/57
Do2Ao1Ex,Recycled gypsum from waste plasterboard: quality protocol,https://www.gov.uk/government/publications/recycled-gypsum-from-waste-plasterboard-quality-protocol/recycled-gypsum-from-waste-plasterboard-quality-protocol,environmentagency,Environment Agency,eng,HTML,When recycled gypsum from waste plasterboard is no longer waste.,12/08/2015,09/04/2021,09/04/2021,Construction Companies,GB-ENG GB-WLS GB-NIR,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39010",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Gypsum
Plasterboard
Waste
Recycling",Active,,,,,,,,,,,,
Zc3Du4Vh,Materials facilities: waste sampling and reporting from October 2024,https://www.gov.uk/guidance/materials-facilities-waste-sampling-and-reporting-from-october-2024,environmentagency,Environment Agency,eng,HTML,"From 1 October 2024, more materials facilities will need to sample and report their waste. Sampling and reporting will be more detailed and more frequent under the amended regulations.",28/06/2023,09/04/2021,09/04/2021,Waste facility operators,GB-ENG GB-WLS,"38110
38120
38210
38220",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Reporting",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/uksi/2023/1156
https://www.legislation.gov.uk/ukpga/1990/43"
Yo0Pz2No,Dispose of waste to landfill,https://www.gov.uk/guidance/dispose-of-waste-to-landfill,environmentagency,Environment Agency,eng,HTML,What you need to do before you send waste to a landfill site.,30/01/2020,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39010",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste disposal
Hazardous Waste
Non-hazardous Waste
Landfill",Active,,,,,,"https://www.gov.uk/government/publications/excise-notice-lft1-a-general-guide-to-landfill-tax/excise-notice-lft1-a-general-guide-to-landfill-tax
https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice/waste-duty-of-care-code-of-practice
https://www.gov.uk/government/publications/environmental-permitting-guidance-the-landfill-directive
https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/government/publications/guidance-on-applying-the-waste-hierarchy
https://www.gov.uk/guidance/manage-waste-upholstered-domestic-seating-containing-pops",,,,,,
Vk0Aw9Jb,Develop a management system: environmental permits,https://www.gov.uk/guidance/develop-a-management-system-environmental-permits,environmentagency,Environment Agency,eng,HTML,How to develop a management system and keep it up to date so that you can carry out activities under an environmental permit.,01/02/2016,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39011",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Environmental Permits
Management",Active,,,,,,https://www.gov.uk/government/publications/fire-prevention-plans-environmental-permits/fire-prevention-plans-environmental-permits,,,,,,
Uw7Qi3Ox,Storing woodchip from untreated wood packaging and using it to make pellets: LRWP 17,https://www.gov.uk/government/publications/low-risk-waste-positions-wood-and-plant-matter/storing-woodchip-from-untreated-wood-packaging-and-using-it-to-make-pellets-lrwp-17,environmentagency,Environment Agency,eng,HTML,This low risk waste position (LRWP) applies if you store woodchip from untreated wood packaging and use it to make pellets.,20/08/2019,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39012",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Wood Pellets
Wood Packaging",Active,,,,,,https://www.gov.uk/guidance/waste-exemption-t6-treating-waste-wood-and-waste-plant-matter-by-chipping-shredding-cutting-or-pulverising,,,,,,
Ay8Vy2Ep,Using waste wood from construction to manufacture finished goods under a U9 exemption: LRWP 73,https://www.gov.uk/government/publications/low-risk-waste-positions-wood-and-plant-matter/using-waste-wood-from-construction-to-manufacture-finished-goods-under-a-u9-exemption-lrwp-73,environmentagency,Environment Agency,eng,HTML,"If you follow the conditions in this low risk waste position (LRWP), you can use waste wood from construction, in addition to other waste wood codes allowed under the U9 waste exemption.",20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Wooden Goods Manufacturing Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39015
16210
16240
16290",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Wood",Active,,,,,,https://www.gov.uk/guidance/waste-exemption-u9-using-waste-to-manufacture-finished-goods,,,,,,
Vb2Ad2Ol,Burning dunnage packing material: LRWP 74,https://www.gov.uk/government/publications/low-risk-waste-positions-wood-and-plant-matter/burning-dunnage-plant-tissue-and-wood-used-to-support-cargo-lrwp-74,environmentagency,Environment Agency,eng,HTML,This low risk waste position (LRWP) allows you to burn dunnage packing material (plant tissue and wood used to support cargo) under a Plant Health Notice at the place where the goods are delivered.,20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Haulage/Freight Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39016
49410",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Dunnage
Burning",Active,,,,,,,,,,,,
Zw9Qi5Gc,Treating waste wood from making panels and furniture under a T6 exemption: LRWP 88,https://www.gov.uk/government/publications/low-risk-waste-positions-wood-and-plant-matter/treating-waste-wood-from-making-panels-and-furniture-under-a-t6-exemption-lrwp-88,environmentagency,Environment Agency,eng,HTML,This low risk waste position (LRWP) applies if you treat waste wood from wood processing and making panels and furniture under a T6 waste exemption.,20/08/2019,09/04/2021,09/04/2021,"Construction Companies
Wooden Goods Manufacturing Companies",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39015
16210
16240
16290",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling",Active,,,,,,https://www.gov.uk/guidance/waste-exemption-t6-treating-waste-wood-and-waste-plant-matter-by-chipping-shredding-cutting-or-pulverising,,,,,,
Ws2Ws0Hq,Storing and managing excavated waste from street works: RPS 299,https://www.gov.uk/government/publications/storing-and-managing-excavated-waste-from-street-works-rps-299,environmentagency,Environment Agency,eng,HTML,"Environment Agency regulatory position on storing, treating, and using excavated utilities wastes classified under RPS 298.",04/06/2024,09/04/2021,09/04/2021,Street Works Construction Companies,GB-ENG,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Road Works",Active,,,,,,"https://www.gov.uk/government/publications/classify-excavated-waste-from-street-and-utility-works-rps-298
https://www.gov.uk/government/publications/waste-classification-technical-guidance",,,,,,
Yu7Uc2Mu,Classify excavated waste from street and utility works: RPS 298,https://www.gov.uk/government/publications/classify-excavated-waste-from-street-and-utility-works-rps-298/classify-excavated-waste-from-street-and-utility-works-rps-298,environmentagency,Environment Agency,eng,HTML,Environment Agency regulatory position on how to classify excavated waste from street works and utility works when you cannot take samples before excavation.,04/06/2024,09/04/2021,09/04/2021,Street Works Construction Companies,GB-ENG,42111,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Road Works",Active,,,,,,"https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/government/publications/storing-and-managing-excavated-waste-from-street-works-rps-299
https://www.gov.uk/government/publications/street-works-permit-schemes-conditions",,,,,,
Df1Ba6Lk,Land contamination risk management (LCRM),https://www.gov.uk/government/publications/land-contamination-risk-management-lcrm,environmentagency,Environment Agency,eng,HTML,"The Environment Agency expects you to follow this guidance if you are managing the risks from land contamination.

If you use this guidance outside England, check with the relevant regulator about its suitability.",08/10/2020,09/04/2021,09/04/2021,"Landowners
Developers
Planners
Construction Companies",GB-ENG GB-WLS GB-NIR,"71112
36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39012",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Pollution
Contamination
Risk Management",Active,,,,,,"https://www.gov.uk/government/publications/land-contamination-risk-management-lcrm/lcrm-before-you-start
https://www.gov.uk/government/publications/land-contamination-risk-management-lcrm/lcrm-stage-1-risk-assessment
https://www.gov.uk/government/publications/land-contamination-risk-management-lcrm/lcrm-stage-2-options-appraisal
https://www.gov.uk/government/publications/land-contamination-risk-management-lcrm/lcrm-stage-3-remediation-and-verification",,,,,,
Tp8Id4Ee,Temporary dewatering from excavations to surface water: RPS 261,https://www.gov.uk/government/publications/temporary-dewatering-from-excavations-to-surface-water/temporary-dewatering-from-excavations-to-surface-water,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position on temporary discharges of uncontaminated water from excavations to surface water without a water discharge activity permit.,07/02/2018,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39012",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Dewatering
Water Pollution/Contamination",Active,,,,,,"https://www.gov.uk/guidance/get-advice-before-you-apply-for-an-environmental-permit
https://www.gov.uk/guidance/water-management-apply-for-a-water-abstraction-or-impoundment-licence",,,,,,https://www.legislation.gov.uk/uksi/2017/1044/regulation
Ek2Ks0Pc,Environmental permits: when and how you are charged,https://www.gov.uk/government/publications/environmental-permitting-charges-guidance/environmental-permitting-charges-guidance,environmentagency,Environment Agency,eng,HTML,How the Environment Agency charges for activities that need an environmental permit and the charges you must pay.,21/03/2018,09/04/2021,09/04/2021,Construction Companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39012",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Permits
Charges",Active,,,,,,"https://www.gov.uk/guidance/a1-installations-environmental-permits
https://www.gov.uk/guidance/waste-environmental-permits
https://www.gov.uk/guidance/discharges-to-surface-water-and-groundwater-environmental-permits
https://www.gov.uk/government/publications/pig-and-poultry-assurance-scheme-intensive-farming/epr-intensive-farming-pig-and-poultry-assurance-scheme
https://www.gov.uk/government/publications/environmental-permits-and-abstraction-licences-tables-of-charges
https://www.gov.uk/guidance/flood-risk-activities-environmental-permits
https://www.gov.uk/government/collections/radioactive-substances-regulation-for-non-nuclear-sites
https://www.gov.uk/government/collections/radioactive-substances-regulation-for-nuclear-sites
https://www.gov.uk/guidance/send-environmental-permit-application-information-in-stages
https://www.gov.uk/government/publications/fire-prevention-plans-environmental-permits/fire-prevention-plans-environmental-permits
https://www.gov.uk/guidance/control-and-monitor-emissions-for-your-environmental-permit
https://www.gov.uk/government/publications/deposit-for-recovery-operators-environmental-permits/waste-recovery-plans-and-deposit-for-recovery-permits",,,,,,https://www.legislation.gov.uk/ukpga/1991/57
Wi9Ue4Ba,Noise and vibration management: environmental permits,https://www.gov.uk/government/publications/noise-and-vibration-management-environmental-permits/noise-and-vibration-management-environmental-permits#when-a-noise-assessment-is-needed,environmentagency,Environment Agency,eng,HTML,"How UK environment agencies assess noise, legal requirements for managing noise, noise impact assessments and noise management plans. This replaces H3 guidance.",23/07/2021,09/04/2021,09/04/2021,Construction Companies,GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39013",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Permits
Noise Pollution
Vibration",Active,,,,,,"https://www.gov.uk/guidance/risk-assessments-for-your-environmental-permit
https://www.gov.uk/guidance/noise-impact-assessments-involving-calculations-or-modelling",,,,,,https://www.legislation.gov.uk/eudr/2018/851
Za2Ee7Rs,Water resources licences: when and how you are charged,https://www.gov.uk/government/publications/water-resources-licences-when-and-how-you-are-charged/water-resources-charges-guidance,environmentagency,Environment Agency,eng,HTML,How to work out charges for water abstraction and impounding licences.,01/04/2022,09/04/2021,09/04/2021,Construction Companies,GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39014",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water abstracting and impounding
Licenses
Charges",Active,,,,,,"https://www.gov.uk/guidance/check-if-you-need-a-licence-to-abstract-water
https://www.gov.uk/government/publications/environmental-permits-and-abstraction-licences-tables-of-charges
https://www.gov.uk/government/publications/environmental-permits-and-abstraction-licences-tables-of-charges/appendix-1-hydroelectric-power-water-abstraction-levels",,,,,,
Ar2Bk5Bt,Replacing the use of 'not otherwise specified' waste codes: RPS 241,https://www.gov.uk/government/publications/waste-codes-not-otherwise-specified-rps-241/waste-codes-not-otherwise-specified-rps-241,environmentagency,Environment Agency,eng,HTML,Environment Agency enforcement position on when you can accept waste with codes that are not listed in your waste authorisation or the quality protocols.,13/09/2021,09/04/2021,09/04/2021,"Construction Companies
",GB-ENG,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39015",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Exemptions",Active,,,,,,"https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/government/publications/street-works-permit-schemes-conditionhttps://www.gov.uk/government/publications/quality-protocol-for-the-production-and-use-of-compost-from-waste
https://www.gov.uk/government/publications/quality-protocol-anaerobic-digestate",,,,,,
Vw5Rn5Gu,Waste duty of care: code of practice,https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice/waste-duty-of-care-code-of-practice,defra,Defra,eng,HTML,This code provides practical guidance on how to meet your waste duty of care requirements in England and Wales.,11/03/2016,09/04/2021,09/04/2021,"Construction Companies
Companies producing waste",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39016",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits
Licenses",Active,,,,,https://assets.publishing.service.gov.uk/media/6274d74bd3bf7f5e3ade6090/Waste_duty_of_care_code_of_practice.pdf,"https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/guidance/hazardous-waste-consignment-note-supplementary-guidance
https://www.gov.uk/government/publications/excise-notice-lft1-a-general-guide-to-landfill-tax/excise-notice-lft1-a-general-guide-to-landfill-tax
https://www.gov.uk/guidance/dispose-of-waste-to-landfill",,,,,,"https://www.legislation.gov.uk/ukpga/1990/43/section/34
https://www.legislation.gov.uk/uksi/2012/811
https://www.legislation.gov.uk/ukpga/1989/14
https://www.legislation.gov.uk/uksi/2011/988"
Ao9Xm5Co,Waste duty of care: code of practice,https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice,defra,Defra,eng,HTML,This code provides practical guidance on how to meet your waste duty of care requirements in England and Wales.,11/03/2016,09/04/2021,09/04/2021,"Construction Companies
Companies producing waste",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39017",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Waste
Recycling
Permits
Licenses",Active,,,,https://www.gov.uk/government/publications/waste-duty-of-care-code-of-practice/waste-duty-of-care-code-of-practice,,"https://www.gov.uk/guidance/register-your-waste-exemptions-environmental-permits
https://www.gov.uk/government/publications/waste-classification-technical-guidance
https://www.gov.uk/guidance/hazardous-waste-consignment-note-supplementary-guidance
https://www.gov.uk/government/publications/excise-notice-lft1-a-general-guide-to-landfill-tax/excise-notice-lft1-a-general-guide-to-landfill-tax
https://www.gov.uk/guidance/dispose-of-waste-to-landfill",,,,,,"https://www.legislation.gov.uk/ukpga/1990/43/section/34
https://www.legislation.gov.uk/uksi/2012/811
https://www.legislation.gov.uk/ukpga/1989/14
https://www.legislation.gov.uk/uksi/2011/988"
Sq4Al5My,Net Zero Pre-construction Work and Small Net Zero Projects Re-opener Governance Document,https://www.ofgem.gov.uk/publications/net-zero-pre-construction-and-small-net-zero-projects-re-opener,officeofgasandelectricitymarkets,Office of Gas and Electricity Markets,eng,HTML,"This document sets out the arrangements for gas transmission and gas distribution network companies to use the Net Zero Pre-construction Work and Small Net Zero Projects Re-opener - including details on the scope, process, and materiality thresholds. It will take effect from 1 April 2021.",30/03/2021,09/04/2021,09/04/2021,Gas Transmission and Distribution Network Operators,GB,"35220
35230",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Net Zero
Construction Projects",Active,,,,,,,,,,,,
Vf0Fc5Ne,ECO2 cavity wall U-value checklist,https://www.ofgem.gov.uk/publications/eco2-cavity-wall-u-value-checklist,officeofgasandelectricitymarkets,Office of Gas and Electricity Markets,eng,HTML,"The cavity wall U-value checklist is designed to:

collate the information needed for cavity wall insulation (CWI) wall U-value calculations
allow the relevant operative(s) to confirm that the data provided is accurate to the best of their knowledge
allow the relevant operative to confirm that the requirements described in RdSAP 2012 (9.92) have been met.
This checklist also contains further information and guidance on our requirements for CWI measures with overwritten U-values.",08/02/2016,09/04/2021,09/04/2021,Gas Companies,GB,"35220
35231",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"U-value
Cavity Walls
Checklist",Active,,,,,,,,,,,,
Ou2Zn8Yj,The statutory and contractual framework,https://www.orr.gov.uk/rail-guidance-compliance/network-access/guidance-policies/track-access-guidance,Office of Rail and Road,Office of Rail and Road,eng,HTML,"This module explains the statutory and contractual framework which applies to the regulation of access to the rail network including The Railways Act 1993 (the Act), The Railways (Access and Management and Licensing of Railways Undertakings) Regulations 2016 (the Regulations) and any parallel application of The Competition Act 1998. It also sets out the relationship with the Network Code.",,09/04/2021,09/04/2021,Rail Operators and Contractor,GB,"42120
49100
49200
49311
52211
52212",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,Railway Access,Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1993/43
https://www.legislation.gov.uk/uksi/2016/645
https://www.legislation.gov.uk/ukpga/1998/41
https://www.legislation.gov.uk/uksi/1994/606"
Cd2Ec8Xl,Beavers: how to manage them and when you need a licence,https://www.gov.uk/guidance/beavers-how-to-manage-them-and-when-you-need-a-licence,naturalengland,Natural England,eng,HTML,How to manage Eurasian beavers on your land without a licence and when you need a licence in England.,02/09/2022,09/04/2021,09/04/2021,Land managers,GB-ENG,"01500
68320",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Beavers
Licenses",Active,,,,,,"https://www.gov.uk/guidance/beavers-licence-to-capture-transport-and-re-release-beavers-or-modify-or-remove-beaver-dams-burrows-and-lodges-cl50
https://www.gov.uk/guidance/beavers-licence-to-modify-or-remove-dams-burrows-and-lodges-cl51
https://www.gov.uk/government/publications/beavers-licence-to-modify-or-remove-dams-cl52",,,,,,
Vx0Nu6Sv,Little whirlpool ramshorn snails: licence to do ditch maintenance (CL14),https://www.gov.uk/government/publications/little-whirlpool-ramshorn-snails-licence-for-ditch-maintenance,naturalengland,Natural England,eng,HTML,Register to use a licence to maintain drainage ditches inhabited by little whirlpool ramshorn snails and find out how to report your actions.,06/10/2014,09/04/2021,09/04/2021,Land managers,GB-ENG,"01500
68321",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Little whirlpool ramshorn snails
Habitat preservation
Licenses
Ditches",Active,,,,,,"https://www.gov.uk/government/publications/little-whirlpool-ramshorn-snails-licence-for-ditch-maintenance/cl14
https://assets.publishing.service.gov.uk/media/5a81eb60e5274a2e8ab56899/CL14_management_protocol.PDF/preview
",,,,,,
Xz4Ux6Le,"Water voles: licence to displace them for work on flood defences, water courses or drainage systems (CL24)",https://www.gov.uk/government/publications/water-voles-licence-to-displace-them-for-work-on-flood-defences-water-courses-or-drainage-systems,naturalengland,Natural England,eng,HTML,Register for a licence to displace water voles to allow internal drainage boards to carry out works that could disturb or damage their burrows and report your actions.,29/02/2016,09/04/2021,09/04/2021,Local Authority Internal Drainage Boards,GB-ENG,37000,Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Voles
Displacement of Animals
Licenses",Active,,,,,,"https://www.gov.uk/government/collections/natterjack-toad-licences
https://www.gov.uk/government/publications/licence-to-sell-protected-plants-and-animals
https://www.gov.uk/government/publications/cormorants-licence-to-kill-or-take-them-to-prevent-damage-to-fisheries
https://www.gov.uk/government/collections/otter-licences
https://www.gov.uk/government/publications/licence-to-sell-animal-specimens-taken-before-october-1981
",,,,,,
Bc1Bs8Ng,Wild birds: surveys and monitoring for onshore wind farms,https://www.gov.uk/guidance/wild-birds-surveys-and-monitoring-for-onshore-wind-farms,naturalengland,Natural England,eng,HTML,"Standing advice for local planning authorities, developers and ecologists for assessing the impacts of wind farms on wild birds.",09/06/2015,09/04/2021,09/04/2021,"Planning Authorities
Developers
Ecologists",GB-ENG GB-WLS GB-NIR,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Wild birds
Wind farms
Animal impact",Active,,,,,,"https://www.gov.uk/construction-near-protected-areas-and-wildlife
https://www.gov.uk/wild-birds-surveys-and-mitigation-for-development-projects
https://www.gov.uk/guidance/wild-birds-protection-surveys-and-licences
",,,,,,
So5Zp9Gv,Prepare a planning proposal to avoid harm or disturbance to protected species,https://www.gov.uk/guidance/prepare-a-planning-proposal-to-avoid-harm-or-disturbance-to-protected-species,naturalengland,Natural England,eng,HTML,How to prepare a planning application when there are protected species on or near a proposed development site.,12/11/2020,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74902",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Planning
Habitat protection
Protected species",Active,,,,,,"https://www.gov.uk/guidance/great-crested-newts-district-level-licensing-for-local-planning-authorities
https://www.gov.uk/guidance/otters-advice-for-making-planning-decisions
https://www.gov.uk/guidance/hazel-dormice-advice-for-making-planning-decisions
https://www.gov.uk/guidance/reptiles-advice-for-making-planning-decisions
",,,,,,
Bj8Uq7Kw,Water voles: licence to displace them (CL31),https://www.gov.uk/government/publications/water-voles-licence-to-displace-them-for-development-projects,naturalengland,Natural England,eng,HTML,Register for a licence to displace water voles to allow work that could disturb them or damage their burrows and report your actions.,01/01/2016,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74903",Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Water Voles
Displacement of Animals
Licenses",Active,,,,,,"https://www.gov.uk/government/publications/otters-licence-to-capture-and-transport-those-trapped-in-fisheries-to-prevent-damage
https://www.gov.uk/government/publications/licence-to-protect-fisheries-from-fish-eating-birds
https://www.gov.uk/government/publications/cormorants-licence-to-kill-or-take-them-to-prevent-damage-to-fisheries",,,,,,
Ok2Ct3Pv,Wild bird general licences: Defra and Natural England's approach,https://www.gov.uk/government/publications/wild-bird-general-licences-defra-and-natural-englands-approach,naturalengland,Natural England,eng,HTML,How Defra and Natural England license the control of certain wild bird species.,14/06/2019,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74904",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Wild Birds
Animal impact",Active,,,,,,https://www.gov.uk/government/consultations/use-of-general-licences-for-the-management-of-certain-wild-birds-a-call-for-evidence,,,,,,
Yz8Qk3Iv,Great crested newts: protection and licences,https://www.gov.uk/guidance/great-crested-newts-protection-surveys-and-licences,naturalengland,Natural England,eng,HTML,What you must do to avoid harming great crested newts and when you'll need a licence.,09/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74905",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Giant crested newts
Licenses
Habitat protection",Active,,,,,,https://www.gov.uk/government/collections/great-crested-newt-licences,,,,,,
Lh5Ln1Ie,Using the nutrient neutrality calculators,https://www.gov.uk/guidance/using-the-nutrient-neutrality-calculators,naturalengland,Natural England,eng,HTML,How to use the calculators to work out a nutrient budget for residential developments in nutrient neutrality catchments.,28/02/2024,09/04/2021,09/04/2021,Residential developers,GB-ENG,41202,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Nutrient Neutrality
Residential Developments",Active,,,,,,"https://www.gov.uk/government/collections/tools-and-resources-for-calculating-nutrient-neutrality
https://www.gov.uk/government/publications/notice-of-designation-of-sensitive-catchment-areas-2024
https://www.gov.uk/government/collections/tools-and-resources-for-calculating-nutrient-neutrality",,,,,,
Bo6Mz3Om,Wildlife licences: when you need to apply,https://www.gov.uk/guidance/wildlife-licences,naturalengland,Natural England,eng,HTML,"Find out which licence you might need to carry out work that affects wildlife and its habitat, how to apply and when you might need to pay.",13/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74905",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Birds",Active,,,,,,"https://www.gov.uk/pest-control-on-your-property
https://www.gov.uk/government/collections/general-licences-for-wildlife-management
https://www.gov.uk/government/publications/non-native-species-apply-for-a-licence-to-release-them
https://www.gov.uk/government/publications/natural-england-privacy-notices/wildlife-licensing-privacy-notice",,,,,,
Di4Pf4Je,Wild birds: protection and licences,https://www.gov.uk/guidance/wild-birds-protection-surveys-and-licences,naturalengland,Natural England,eng,HTML,What you must do to avoid harming birds and when you'll need a licence.,13/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Birds",Active,,,,,,"https://www.gov.uk/government/publications/organisational-licence-for-routine-work-affecting-protected-species
https://www.gov.uk/government/publications/chargeable-services-general-terms-and-conditions
https://www.gov.uk/guidance/prevent-wild-birds-damaging-your-land-farm-or-business
https://www.gov.uk/guidance/sites-of-special-scientific-interest-public-body-responsibilities",,,,,,
Wm6Ce0Gy,Apply for a screening decision: restructuring rural land (form EIA1a),https://www.gov.uk/government/publications/application-for-an-environmental-impact-assessment-screening-decision-eia1a,naturalengland,Natural England,eng,HTML,Use this form to apply for an Environmental Impact Assessment (EIA) (Agriculture) screening decision for projects that will restructure rural land.,07/08/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Screening Decisions
EIA
Environmental Impact Assessment",Active,,,,,,"https://www.gov.uk/government/publications/changing-uncultivated-semi-natural-and-rural-land-when-you-need-permission
https://www.gov.uk/government/publications/application-for-an-environmental-impact-assessment-screening-decision-eia1
https://www.gov.uk/government/publications/request-a-consultation-to-change-uncultivated-semi-natural-or-rural-land
https://www.gov.uk/government/publications/agent-authorisation-form-change-uncultivated-semi-natural-and-rural-land
",,,,,,
Qg2Tt5Qa,Protected species licences: when to include a reasoned statement with your application,https://www.gov.uk/government/publications/reasoned-statement-to-support-a-mitigation-licence-application,naturalengland,Natural England,eng,HTML,Use the correct form to explain why your application meets the licence criteria and that there's no satisfactory alternative to your planned activity.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Protected soecies",Active,,,,,,"https://www.gov.uk/government/publications/reference-to-support-a-protected-species-licence
https://www.gov.uk/government/publications/bats-apply-for-a-mitigation-licence
https://www.gov.uk/government/publications/water-voles-apply-for-a-mitigation-licence-a11
https://www.gov.uk/government/publications/great-crested-newts-apply-for-a-mitigation-licence",,,,,,
Ax0Ca9Rx,Natterjack toads: apply for a mitigation licence (A44),https://www.gov.uk/government/publications/natterjack-toads-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,Apply for a licence to carry out work that may affect natterjack toads and find out how to report your actions.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Natterjack Toads
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/terms-and-conditions-for-paying-for-a-wildlife-licence
https://www.gov.uk/government/publications/great-crested-newts-district-level-licensing-schemes-for-developers
https://www.gov.uk/government/publications/great-crested-newts-apply-for-a-mitigation-licence",,,,,,
In5Tr8Mn,Smooth snakes and sand lizards: apply for a mitigation licence (A46),https://www.gov.uk/government/publications/smooth-snakes-and-sand-lizards-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,Apply for a licence to carry out work that may affect smooth snakes or sand lizards and find out how to report your actions.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Smooth snakes
Sand lizards
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/method-statement-to-support-a-mitigation-licence-application
https://www.gov.uk/government/publications/natterjack-toads-apply-for-a-mitigation-licence
https://www.gov.uk/government/publications/great-crested-newts-report-survey-or-research-licence-actions
https://www.gov.uk/government/publications/great-crested-newts-survey-or-research-licence-level-2
",,,,,,
Tq1Iv4Sw,Organisational licence for routine work affecting protected species,https://www.gov.uk/government/publications/organisational-licence-for-routine-work-affecting-protected-species,naturalengland,Natural England,eng,HTML,"Apply for an organisational licence for your business for routine activities that affect protected species, and find out if you need to pay.",23/04/2019,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Routine works
Protected species
Licenses",Active,,,,,,"https://www.gov.uk/government/publications/chargeable-services-general-terms-and-conditions
https://www.gov.uk/guidance/prevent-wild-birds-damaging-your-land-farm-or-business
https://www.gov.uk/government/publications/wild-birds-licence-to-kill-or-take-for-public-health-or-safety-gl41
https://www.gov.uk/government/publications/wild-birds-licence-to-kill-or-take-to-prevent-serious-damage-gl42
",,,,,,
Ym5Sd9Ul,Water voles: apply for a mitigation licence (A11),https://www.gov.uk/government/publications/water-voles-apply-for-a-mitigation-licence-a11,naturalengland,Natural England,eng,HTML,Apply for a licence to carry out work that may affect water voles. Find out if you need to pay for the licence and how to report your actions.,21/12/2022,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Water voles
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/terms-and-conditions-for-paying-for-a-wildlife-licence
https://www.gov.uk/government/publications/great-crested-newts-district-level-licensing-schemes-for-developers
https://www.gov.uk/government/publications/edible-dormice-licence-to-trap-them
https://www.gov.uk/government/publications/reference-to-support-a-protected-species-licence",,,,,,
Ul2Rw5Tu,Otters: apply for a mitigation licence (A45),https://www.gov.uk/government/publications/otters-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,Apply for a licence to do development or other work that may affect otters and find out how to report your actions.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Otters
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/great-crested-newts-district-level-licensing-schemes-for-developers
https://www.gov.uk/government/publications/great-crested-newts-report-survey-or-research-licence-actions
https://www.gov.uk/government/publications/great-crested-newts-survey-or-research-licence-level-2
https://www.gov.uk/government/publications/hazel-dormice-survey-or-research-licence-level-2
https://www.gov.uk/government/publications/natterjack-toads-apply-for-a-mitigation-licence",,,,,,
Kn4Lu1Bz,Hazel dormice: apply for a mitigation licence (A35),https://www.gov.uk/government/publications/hazel-dormice-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,"Apply for a licence to carry out work that may affect hazel dormice, find out if you need to pay and how to report your actions.",06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Hazel dormice
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/natterjack-toads-apply-for-a-mitigation-licence
https://www.gov.uk/government/publications/method-statement-to-support-a-mitigation-licence-application
https://www.gov.uk/government/publications/great-crested-newts-district-level-licensing-schemes-for-developers
https://www.gov.uk/government/publications/great-crested-newts-apply-for-a-mitigation-licence
https://www.gov.uk/guidance/hazel-dormice-protection-surveys-and-licences",,,,,,
Py0Ow7Vc,Protected species: apply for a mitigation licence (A05 and A05a),https://www.gov.uk/government/publications/protected-species-apply-for-a-mitigation-licence-a05-and-a05a,naturalengland,Natural England,eng,HTML,"Apply for a licence to carry out work that may affect species protected under the Wildlife and Countryside Act 1981, find out if you need to pay and how to report your actions.",30/09/2022,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Licenses
Protected species
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/edible-dormice-licence-to-trap-them
https://www.gov.uk/government/publications/badgers-survey-or-research-licence",,,,,,
Er5Yy6Oo,Charged environmental advice service request form,https://www.gov.uk/government/publications/charged-environmental-advice-service-request-form,naturalengland,Natural England,eng,HTML,Use this form to request Natural England's advice on planning applications and applications for nationally significant infrastructure projects.,12/10/2015,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Advice request
Planning applications
Nationally significant infrastructure",Active,,,,,,"https://www.gov.uk/government/publications/planning-and-marine-licence-advice-standard-terms-for-our-charges
https://www.gov.uk/guidance/developers-get-environmental-advice-on-your-planning-proposals",,,,,,
Hs8Ae0Ze,Badgers: protection and licences,https://www.gov.uk/guidance/badgers-protection-surveys-and-licences,naturalengland,Natural England,eng,HTML,What you must do to avoid harming badgers and when you'll need a licence.,13/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Badgers
Habitat protection
Licenses
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-to-prevent-damage
https://www.gov.uk/guidance/badgers-advice-for-making-planning-decisions
https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-for-forestry-purposes
https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-during-archaeological-digs",,,,,,
Lr8Ne1Lm,Badgers: licence to interfere with setts for development purposes (A24 and LR24),https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-for-development-purposes,naturalengland,Natural England,eng,HTML,Apply for a licence to interfere with badger setts during development work and find out how to report your actions.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Badgers
Habitat protection
Licenses
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-to-prevent-damage
https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-for-forestry-purposes
https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-during-archaeological-digs
https://www.gov.uk/government/publications/badgers-licence-to-interfere-with-setts-for-drainage-purposes
",,,,,,
Tv3Hw5Ry,Great crested newts: apply for a mitigation licence (A14),https://www.gov.uk/government/publications/great-crested-newts-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,Apply for a licence to do development or other work that may affect great crested newts and find out how much you may need to pay.,06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Great crested newts
Habitat protection
Licenses
Harm mitigation",Active,,,,,,"https://www.gov.uk/guidance/great-crested-newts-protection-surveys-and-licences
https://www.gov.uk/guidance/european-protected-species-policies-for-mitigation-licences
https://www.gov.uk/government/publications/hazel-dormice-apply-for-a-mitigation-licence
https://www.gov.uk/government/publications/natterjack-toads-apply-for-a-mitigation-licence
https://www.gov.uk/government/publications/smooth-snakes-and-sand-lizards-apply-for-a-mitigation-licence",,,,,,
Br8Jg4Qw,Bats: protection and licences,https://www.gov.uk/guidance/bats-protection-surveys-and-licences,naturalengland,Natural England,eng,HTML,What you must do to avoid harming bats and when you'll need a licence.,08/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Bats
Habitat protection
Licenses
Harm mitigation",Active,,,,,,"https://www.gov.uk/guidance/bat-roosts-use-of-chemical-pest-control-products-and-timber-treatments-in-or-near-them
https://www.gov.uk/government/publications/bats-licence-to-interfere-with-bat-roosts-cl21
https://www.gov.uk/guidance/hazel-dormice-protection-surveys-and-licences",,,,,,
Vs8Pe6Nu,Bats: apply for a mitigation licence (A13),https://www.gov.uk/government/publications/bats-apply-for-a-mitigation-licence,naturalengland,Natural England,eng,HTML,"Apply for a licence to carry out work that may affect bats, find out if you need to pay and how to report your actions.",06/10/2014,09/04/2021,09/04/2021,"Developers
Construction Companies
Owners of SSSI",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Bats
Habitat protection
Licenses
Harm mitigation",Active,,,,,,"https://www.gov.uk/government/publications/great-crested-newts-apply-for-a-mitigation-licence
https://www.gov.uk/guidance/bats-protection-surveys-and-licences
https://www.gov.uk/guidance/european-protected-species-policies-for-mitigation-licences",,,,,,
Rb5Vm4Ff,Give notice and get consent for a planned activity on a SSSI,https://www.gov.uk/government/publications/request-permission-for-works-or-an-activity-on-an-sssi,naturalengland,Natural England,eng,HTML,Owners and occupiers should use this form to give notice of a planned activity on a site of special scientific interest (SSSI) that needs Natural England's permission.,02/06/2016,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"SSSI
Planned activity
Consent",Active,,,,,,"https://www.gov.uk/guidance/protected-areas-sites-of-special-scientific-interest
https://www.gov.uk/government/publications/give-notice-and-get-assent-for-a-planned-activity-on-or-near-an-sssi
https://www.gov.uk/government/publications/quick-check-service-on-a-sssi-assent-notice
https://www.gov.uk/government/publications/sites-of-special-scientific-interest-assent-advice-request-form
",,,,,,
Fg5Ys2Am,Environmental impact assessment inspection,https://www.gov.uk/guidance/environmental-impact-assessment-inspection,naturalengland,Natural England,eng,HTML,Information for landowners about inspections carried out to decide if an environmental impact assessment is needed or regulations may have been broken.,12/01/2016,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Impact assessment
Breach of regulations",Active,,,,,,"https://www.gov.uk/government/organisations/office-for-product-safety-and-standards/about/research
https://www.gov.uk/government/collections/product-safety-research
https://www.gov.uk/government/publications/regulatory-research-dementia-workshop-conclusions
https://www.gov.uk/government/publications/characteristics-of-modern-domestic-fire-scenarios
https://www.gov.uk/government/collections/farming-inspections
",,,,,,
Ow8Sn4Fl,Developers: get environmental advice on your planning proposals,https://www.gov.uk/guidance/developers-get-environmental-advice-on-your-planning-proposals,naturalengland,Natural England,eng,HTML,"How developers can get advice on Nationally Significant Infrastructure Projects (NSIPs) and applications for planning, permission in principle and technical details consent.",29/03/2015,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Consultations
Permits
Impact Assessments",Active,,,,,,"https://www.gov.uk/guidance/construction-near-protected-areas-and-wildlife#protected-areas
https://magic.defra.gov.uk/home.htm
https://www.gov.uk/guidance/construction-near-protected-areas-and-wildlife
https://www.gov.uk/government/publications/agricultural-land-assess-proposals-for-development
https://www.gov.uk/guidance/protected-species-how-to-review-planning-applications
https://www.gov.uk/guidance/nutrient-mitigation-check-if-you-need-environmental-permissions
https://www.gov.uk/government/publications/planning-and-marine-licence-advice-standard-terms-for-our-charges",,,,,,
Xc1Rp7Wm,Carrying out works on common land,https://www.gov.uk/guidance/carrying-out-works-on-common-land,naturalengland,Natural England,eng,HTML,"When you need to apply for consent, how to apply, and the works that you can do without consent.",28/03/2015,09/04/2021,09/04/2021,"Developers
Construction Companies",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Consent for works
Common land",Active,,,,,,"http://www.acraew.org.uk/commons-registration-authorities-contact-details
https://www.gov.uk/government/publications/common-land-consents-policy
https://www.gov.uk/guidance/set-up-a-commons-council
https://www.gov.uk/guidance/common-land-and-town-or-village-greens-access-your-property-by-vehicle
https://www.gov.uk/government/publications/common-land-guidance-sheet-1a-consent-to-construct-works-on-common-land",,,,,,
Th5Wb3Tx,Habitats regulations assessments: protecting a European site,https://www.gov.uk/guidance/habitats-regulations-assessments-protecting-a-european-site,naturalengland,Natural England,eng,HTML,How a competent authority must decide if a plan or project proposal that affects a European site can go ahead.,24/02/2021,09/04/2021,09/04/2021,Local authorities,GB-ENG,,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"European sites
Planning
Aprroval",Active,,,,,,"https://www.gov.uk/guidance/habitats-regulations-assessments-protecting-a-european-site#European-sites
https://www.gov.uk/government/organisations
https://www.gov.uk/guidance/conservation-objectives-for-land-based-protected-sites-in-england-how-to-use-the-site-advice
https://www.gov.uk/guidance/duty-to-protect-conserve-and-restore-european-sites
https://www.gov.uk/government/publications/habitats-regulations-assessment-derogation-notice
https://www.gov.uk/guidance/duty-to-protect-conserve-and-restore-european-sites
",,,,,,
Hm1Uj7Di,Countryside hedgerow protection: removing hedgerows,https://www.gov.uk/guidance/countryside-hedgerows-regulation-and-management,naturalengland,Natural England,eng,HTML,Find out if you can remove or work on countryside hedgerows.,11/09/2014,09/04/2021,09/04/2021,"Developers
Construction Companies
Land managers
Landscape gardeners",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81300",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Hedgerows
Pretected countryside
Unlimited fine
Removal of hedgerows",Active,,,,,,"https://www.gov.uk/guidance/planning-applications-affecting-trees-and-woodland
https://www.gov.uk/government/collections/forestry-commission-operations-notes-england
https://www.gov.uk/government/publications/hedgerows-and-boundaries-grant-countryside-stewardship
https://www.gov.uk/guidance/forestry-project-checks-all-projects
https://www.gov.uk/guidance/how-to-benefit-species-and-habitats-biodiversity-in-your-woodland
http://jncc.defra.gov.uk/page-4
https://www.gov.uk/guidance/hedgerow-management-rules-cutting-and-trimming
https://www.gov.uk/find-local-council",,,,,,
Vy4Hv3Ss,Sites of special scientific interest: managing your land,https://www.gov.uk/guidance/protected-areas-sites-of-special-scientific-interest,naturalengland,Natural England,eng,HTML,When you need consent for a proposed operation or management change on land in a SSSI and how to apply.,24/04/2013,09/04/2021,09/04/2021,"Developers
Construction Companies
Land managers
Landscape gardeners",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81301",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Sites of special scientific interest
SSSI
Land use changes",Active,,,,,,,,,,,,
Ze8Yv9Jq,How to stop Japanese knotweed from spreading,https://www.gov.uk/guidance/prevent-japanese-knotweed-from-spreading,naturalengland,Natural England,eng,HTML,"How to identify, stop the spread and dispose of Japanese knotweed in England.",30/03/2016,09/04/2021,09/04/2021,"Developers
Construction Companies
Land managers
Landscape gardeners",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81302",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Japanese Knotweed
Invasive species
Non-native plants",Active,,,,,,,,,,,,
Qx6Xi6Op,Open access land and the coastal margin: how to restrict public access,https://www.gov.uk/guidance/open-access-land-and-the-coastal-margin-how-to-restrict-public-access,naturalengland,Natural England,eng,HTML,"As an owner or manager of land, understand how to restrict public access for land management, public safety or fire prevention reasons.",27/03/2015,09/04/2021,09/04/2021,"Landowners
Land managers",GB-ENG,,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Countryside Access
Limiting Access",Active,,,,,,,,,,,,
Fd2Qn9Xl,"Open access land: management, rights and responsibilities",https://www.gov.uk/guidance/open-access-land-management-rights-and-responsibilities,naturalengland,Natural England,eng,HTML,"As a land owner or manager, find out about your responsibilities and how to manage public access.",17/09/2014,09/04/2021,09/04/2021,"Landowners
Land managers",GB-ENG,,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Countryside Access
Limiting Access",Active,,,,,,,,,,,,
Xl0Hp9Pr,The Countryside Code: advice for land managers,https://www.gov.uk/government/publications/the-countryside-code/the-countryside-code-advice-for-land-managers,naturalengland,Natural England,eng,HTML,Know your rights and responsibilities,18/09/2014,09/04/2021,09/04/2021,"Landowners
Land managers",GB-ENG GB-WLS,,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Rights of way
Land managers
Visitor access",Active,,,,,,,,,,,,
Rp4Fa5Or,Public rights of way: landowner responsibilities,https://www.gov.uk/guidance/public-rights-of-way-landowner-responsibilities,naturalengland,Natural England,eng,HTML,"As the owner or occupier of land with a public right of way across it, you must keep the route visible and not obstruct or endanger users.",11/09/2014,09/04/2021,09/04/2021,"Landowners
Land managers",GB-ENG,,Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Countryside Code
Land managers
Visitor access",Active,,,,,,,,,,,,
Mk3Px9Hl,3D Laser Scanning for Heritage,https://historicengland.org.uk/images-books/publications/3d-laser-scanning-heritage/,historicengland,Historic England,eng,HTML,"This guidance should assist archaeologists, conservators and other cultural heritage professionals unfamiliar with the approach in making the best possible use of 3D Laser Scanning.",12/09/2014,09/04/2021,09/04/2021,"Archaeologists
Conservators
Architects",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81302
71111",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"3D Laser Scanning
Heritage Protection",Active,,,,,,"https://historicengland.org.uk/images-books/publications/bim-for-heritage/
https://historicengland.org.uk/images-books/publications/photogrammetric-applications-for-cultural-heritage/
https://historicengland.org.uk/images-books/publications/using-airborne-lidar-in-archaeological-survey/
https://historicengland.org.uk/images-books/publications/multi-light-imaging-heritage-applications/
",,,,,https://historicengland.org.uk/images-books/publications/3d-laser-scanning-heritage/heag155-3d-laser-scanning/,
Pq9Ts5Wl,Adapting Traditional Farm Buildings,https://historicengland.org.uk/images-books/publications/adapting-traditional-farm-buildings/,historicengland,Historic England,eng,HTML,"This advice is aimed at owners of farm buildings, building professionals and local authority planning and conservation officers. It explains how significance can be retained and enhanced through well-informed maintenance and sympathetic development, provided that repairs, design and implementation are carried out to a high standard.",13/09/2014,09/04/2021,09/04/2021,"Owners of farm buildings
Construction companies
Local planning authorities",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81302
71112
01500
01621",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Farm Building
Conservation
Repair and Preservation",Active,,,,,,"https://historicengland.org.uk/images-books/publications/adapting-traditional-farm-buildings/heag158-adapting-traditional-farm-buildings/
https://historicengland.org.uk/images-books/publications/adaptive-reuse-traditional-farm-buildings-advice-note-9/
https://historicengland.org.uk/images-books/publications/maintenance-repair-trad-farm-buildings/",,,,,,
Rd8Zh9We,The Adaptive Reuse of Traditional Farm Buildings,https://historicengland.org.uk/images-books/publications/adaptive-reuse-traditional-farm-buildings-advice-note-9/,historicengland,Historic England,eng,HTML,"This advice is aimed at owners of farm buildings, building professionals and local authority planning and conservation officers. It explains how significance can be retained and enhanced through well-informed maintenance and sympathetic development, provided that repairs, design and implementation are carried out to a high standard.",14/09/2014,09/04/2021,09/04/2021,"Owners of farm buildings
Construction companies
Local planning authorities",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907
81302
71112
01500
01622",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Farm Building
Conservation
Repair and Preservation",Active,,,,,,"https://historicengland.org.uk/images-books/publications/adaptive-reuse-traditional-farm-buildings-advice-note-9/heag156-adaptive-reuse-farm-buildings/
https://historicengland.org.uk/images-books/publications/adapting-traditional-farm-buildings/
https://historicengland.org.uk/images-books/publications/maintenance-repair-trad-farm-buildings/
",,,,,,
Dk5Lz2Rg,BIM for Heritage,https://historicengland.org.uk/images-books/publications/bim-for-heritage/,historicengland,Historic England,eng,HTML,"This publication addresses the issues surrounding the production and use of BIM for historic buildings, and provides information about guidance and standards available elsewhere for managing a building's entire life cycle effectively.",15/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74906",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Digital Models
Building Maintenance
Heritage Maintenance",Active,,,,,,"https://historicengland.org.uk/images-books/publications/bim-for-heritage/heag-154-bim-for-heritage/
https://historicengland.org.uk/images-books/publications/bim-for-heritage-aim/
https://historicengland.org.uk/images-books/publications/graphical-and-plane-table-survey-archaeological-earthworks/
https://historicengland.org.uk/images-books/publications/3d-laser-scanning-heritage/",,,,,,
Ol7Nw9Ll,BIM for Heritage - Developing the Asset Information Model,https://historicengland.org.uk/images-books/publications/bim-for-heritage-aim/,historicengland,Historic England,eng,HTML,"This  guidance is on BIM for heritage and focuses on heritage asset management, in particular conservation repair and maintenance, and suggests that the first task when adopting a BIM information management approach is to develop an Asset Information Model (AIM).",16/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74907",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Digital Models
Building Maintenance
Heritage Maintenance",Active,,,,,,https://historicengland.org.uk/images-books/publications/bim-for-heritage-aim/heag271-bim-developing-asset-info-model/,,,,,,
Lb0Zm7Ks,Briefing Note on National Listed Building Consent Orders,https://historicengland.org.uk/images-books/publications/notes-listed-building-consent-orders/,historicengland,Historic England,eng,HTML,"This document provides information on national Listed Building Consent Orders (LBCO) for local planning authorities, heritage practitioners and owners of listed buildings who may in due course be affected by an LBCO. It does not provide advice on their setting up or operation, as they are the responsibility of the Secretary of State.",17/09/2014,09/04/2021,09/04/2021,"Construction companies
Local Authorities",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74908",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Listed Building Consent Orders
Heritage Buildings",Active,,,,,,"https://historicengland.org.uk/images-books/publications/notes-listed-building-consent-orders/heag022-national-listed-building-consent-orders/
https://historicengland.org.uk/advice/planning/consents/err-act-2013/
https://historicengland.org.uk/listing/what-is-designation/listed-buildings/
",,,,,,
Sq4Oq4Co,Church Roof Replacement Using Terne-coated Stainless Steel,https://historicengland.org.uk/images-books/publications/church-roof-replacement-terne-coated-stainless-steel/,historicengland,Historic England,eng,HTML,The Guidance Note considers eight design and specification issues that frequently arise when considering the use of TCSS to replace stolen lead roofing on churches. It presents the findings of the survey and provides technical guidance on addressing each of the issues.,18/09/2014,09/04/2021,09/04/2021,"Construction companies
Local Authorities",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74909",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Churches
Lead Roofing
Stainless Steel",Active,,,,,,"https://historicengland.org.uk/images-books/publications/church-roof-replacement-terne-coated-stainless-steel/heag280-church-roof-replacement-terne-coated-stainless-steel-rev2/
https://historicengland.org.uk/images-books/publications/theft-metal-church-roofs-prevention-response/
https://historicengland.org.uk/images-books/publications/theft-metal-church-roofs-replacement-materials/
https://historicengland.org.uk/advice/caring-for-heritage/heritage-crime/
https://historicengland.org.uk/advice/caring-for-heritage/places-of-worship/places-of-worship-at-risk/metal-theft/",,,,,,
Ce2Aa2Xu,Commercial Renewable Energy Development and the Historic Environment,https://historicengland.org.uk/images-books/publications/commercial-renewable-energy-development-historic-environment-advice-note-15,historicengland,Historic England,eng,HTML,"This Historic England Advice Note describes the potential impacts on the historic environment of commercial renewable energy proposals, which could occupy large areas of land or sea. It is written for all of those involved in commercial renewable energy development, helping them to give appropriate consideration to heritage issues.",19/09/2014,09/04/2021,09/04/2021,Renewable Energy Construction Companies,,"42210
42220
42990",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Wind Power
Solar Power
Biomass waste",Active,,,,,,https://historicengland.org.uk/images-books/publications/commercial-renewable-energy-development-historic-environment-advice-note-15/heag302-commercial-renewable-energy-development-historic-environment/,,,,,,
Wu5Ge8Ts,"Conservation Area Appraisal, Designation and Management",https://historicengland.org.uk/images-books/publications/conservation-area-appraisal-designation-management-advice-note-1/,historicengland,Historic England,eng,HTML,"This advice note supports the management of change in a way that conserves and enhances the character and appearance of historic areas through conservation area appraisal, designation and management.",20/09/2014,09/04/2021,09/04/2021,"Construction companies
Local Authorities",GB-ENG,"41100
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38119
74909",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Conservation Areas
Town Planning
Building Management",Active,,,,,,https://historicengland.org.uk/images-books/publications/conservation-area-appraisal-designation-management-advice-note-1/heag-268-conservation-area-appraisal-designation-management/,,,,,,
Bw5Ai6Ax,"Conservation Principles, Policies and Guidance",https://historicengland.org.uk/images-books/publications/conservation-principles-sustainable-management-historic-environment/,historicengland,Historic England,eng,HTML,"This guidance is intended for anyone interested in or responsible for the care of war memorials. This might include parish, local and district councils, conservation professionals, contractors, statutory bodies, volunteer groups or private owners. Although the guidance covers the setting of war memorials, more detailed information on landscape issues can be found in the publication The Conservation and Management of War Memorial Landscapes. When it refers to 'custodians', the document is addressing anyone who has taken on formal responsibility for a war memorial, whether or not they are its legal owner.",21/09/2014,09/04/2021,09/04/2021,"Local Authorities
Construction Companies",GB-ENG,43999,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"War Memorials
Maintenance
Restoration",Active,,,,,,"https://historicengland.org.uk/images-books/publications/conservation-principles-sustainable-management-historic-environment/conservationprinciplespoliciesandguidanceapril08web/
https://historicengland.org.uk/advice/your-home/improvement/practical-tips/
https://historicengland.org.uk/advice/constructive-conservation/conservation-principles/
https://historicengland.org.uk/advice/caring-for-heritage/places-of-worship/making-changes/
",,,,,,
Tx3Qb3Ee,"The Conservation, Repair and Management of War Memorials",https://historicengland.org.uk/images-books/publications/conservation-repair-management-war-memorials/,historicengland,Historic England,eng,HTML,"This guide is for local authorities, owners and others involved in the conservation of Georgian and Victorian / early 20th century terraced housing. It gives a historic overview of terraced housing and identifies important features of different types of terrace.",22/09/2014,09/04/2021,09/04/2021,"Local Authorities
Construction Companies",GB-ENG,41202,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Georgian construction
Victorian construction
Conservation of houses",Active,,,,,,"https://historicengland.org.uk/images-books/publications/conservation-repair-management-war-memorials/heag006-war-memorials/
https://historicengland.org.uk/images-books/publications/conservation-management-war-memorial-landscapes-updated/
https://historicengland.org.uk/images-books/publications/conserving-war-memorials-cleaning/
https://historicengland.org.uk/images-books/publications/conserving-war-memorials-inscriptions/",,,,,,
Hg1Qq8Xn,Conserving Georgian and Victorian terraced housing,https://historicengland.org.uk/images-books/publications/conserving-georgian-victorian-terraced-housing/,historicengland,Historic England,eng,HTML,"This technical advice note describes good practice for cleaning war memorials, outlining a step-by-step approach to aid decisions on whether cleaning is necessary and the range of techniques available. It includes where to get further help and advice.",23/09/2014,09/04/2021,09/04/2021,"Local Authorities
Construction Companies",GB-ENG,43999,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"War Memorials
Maintenance
Restoration
Cleaning",Active,,,,,,"https://historicengland.org.uk/images-books/publications/conserving-georgian-victorian-terraced-housing/heag277-conserving-georgian-and-victorian-terraced-housing/
https://historicengland.org.uk/advice/your-home/improvement/
https://historicengland.org.uk/advice/planning/planning-system/
https://historicengland.org.uk/whats-new/features/georgians/",,,,,,
Ts0Ue7Tb,Conserving War Memorials: Cleaning,https://historicengland.org.uk/images-books/publications/conserving-war-memorials-cleaning/,historicengland,Historic England,eng,HTML,This technical advice note describes good practice for conserving inscriptions on war memorials. It illustrates the types of inscriptions commonly found and explains how and why they deteriorate. It outlines how to assess the condition of the inscriptions and describes a range of methods for conservation. Information about sources of further help and advice is also included.,24/09/2014,09/04/2021,09/04/2021,"Local Authorities
Construction Companies",GB-ENG,44000,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"War Memorials
Maintenance
Restoration
Cleaning",Active,,,,,,"https://historicengland.org.uk/images-books/publications/conserving-war-memorials-cleaning/heag147-conserving-war-memorials/
https://historicengland.org.uk/images-books/publications/conservation-repair-management-war-memorials/
https://historicengland.org.uk/images-books/publications/conservation-management-war-memorial-landscapes-updated/
",,,,,,
Nd1Ck7Cx,Conserving War Memorials: Inscriptions,https://historicengland.org.uk/images-books/publications/conserving-war-memorials-inscriptions/,historicengland,Historic England,eng,HTML,"This technical note describes good practice for diagnosing and understanding the structural problems found in war memorials, with a focus on freestanding masonry and memorials built of concrete. It details what specialist advice may be required, and the steps that might follow diagnosis, including structural monitoring, emergency works and structural repair options. It also indicates where to get further help and advice.",25/09/2014,09/04/2021,09/04/2021,"Local Authorities
Construction Companies",GB-ENG,44001,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"War Memorials
Maintenance
Restoration
Cleaning",Active,,,,,,https://historicengland.org.uk/images-books/publications/conserving-war-memorials-inscriptions/heag274-conserving-war-memorials-inscriptions/,,,,,,
Py0Wf3Fg,Conserving War Memorials: Structural Problems and Repairs,https://historicengland.org.uk/images-books/publications/conserving-war-memorials-structural/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for improving the thermal performance of existing windows and doors by draught-proofing. Draught-proofing is one of the most cost effective and least intrusive ways of improving the comfort of occupants and reducing energy used for heating with little or no change to a building's appearance. It also has the added benefit of helping to reduce noise and keeping out dust.",26/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41202,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Draught-proofing
Thermal Peformance
Windows
Doors",Active,,,,,,https://historicengland.org.uk/images-books/publications/conserving-war-memorials-structural/heag169-conserving-war-memorials-structural/,,,,,,
Je4Yb6Tp,Energy Efficiency and Historic Buildings: Draught-proofing windows and doors,https://historicengland.org.uk/images-books/publications/eehb-draught-proofing-windows-doors/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for improving the thermal performance of buildings built with early forms of masonry cavity walls dating from before the Second World War.",27/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41203,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Cavity walls
Energy efficiency
Pre-WWII",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-draught-proofing-windows-doors/heag084-draughtproofing/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-insulating-timber-framed-walls/
https://historicengland.org.uk/images-books/publications/eehb-early-cavity-walls/
https://historicengland.org.uk/images-books/publications/eehb-insulating-thatched-roofs/
",,,,,,
Az1Em6Kx,Energy Efficiency and Historic Buildings: Early cavity walls,https://historicengland.org.uk/images-books/publications/eehb-early-cavity-walls/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for insulating dormer windows. Dormers come in a large variety of shapes, sizes and materials and can be a particularly difficult element to insulate. However, if insulation is omitted or is poorly detailed then the energy performance of the whole roof can be compromised.",28/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41204,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Dormer windows
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-early-cavity-walls/heag083-early-cavity-walls/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-draught-proofing-windows-doors/
",,,,,,
Fs9Fm4Sk,Energy Efficiency and Historic Buildings: How to Improve Energy Efficiency,https://historicengland.org.uk/images-books/publications/eehb-how-to-improve-energy-efficiency/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for improving the thermal performance of flat roofs by the addition or upgrading of insulation. Adding insulation to flat roofs can lead to a significant reduction in heat loss but thought and care is needed to make sure this is effective and does not cause problems.",29/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41205,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Flat roofing
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/advice/technical-advice/retrofit-and-energy-efficiency-in-historic-buildings/traditional-buildings-and-energy-efficiency/
https://historicengland.org.uk/advice/technical-advice/retrofit-and-energy-efficiency-in-historic-buildings/resilient-rainwater-systems/
https://historicengland.org.uk/advice/technical-advice/retrofit-and-energy-efficiency-in-historic-buildings/modifying-windows-and-doors-in-historic-buildings/
",,,,,,
Oi6Mx7Sv,Energy Efficiency and Historic Buildings: Insulating dormer windows  ,https://historicengland.org.uk/images-books/publications/eehb-insulating-dormer-windows/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for insulating pitched roofs at ceiling level. When insulation is placed in this position, the roof is often referred to as a 'cold roof'. Insulating above the top floor ceiling is one of the easiest and cheapest means of improving the energy efficiency of buildings and such work can be carried out successfully in older buildings if approached with some care. Even very thick layers of insulation will not cause problems if installed with materials that are compatible with the existing construction. However, the installation can be made much more difficult if part of the ceiling to the top floor rooms is within a pitched roof space.",30/09/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41206,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Pitched roofing
Cold roofs
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-dormer-windows/heag082-dormer-windows/
https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-rafter-level-warm-roofs/
https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-ceiling-level-cold-roofs/",,,,,,
Vi1Zs6Du,Energy Efficiency and Historic Buildings: Insulating flat roofs,https://historicengland.org.uk/images-books/publications/eehb-insulating-flat-roofs/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the methods, materials and risks involved with insulating solid ground floors. The energy savings resulting from insulating solid ground floors can in many cases be of marginal benefit when the cost and disruption to the building fabric are considered. Insulating other building elements is likely to produce greater benefits in energy efficiency for significantly less cost.",01/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41207,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Solid ground floors
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-flat-roofs/heag078-flat-roofs/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
",,,,,,
Ol8Ou8Oy,Energy Efficiency and Historic Buildings: Insulating pitched roofs at ceiling level-cold roofs,https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-ceiling-level-cold-roofs/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for insulating solid masonry walls. Traditional solid wall construction is often the most difficult and in many cases the least cost effective part of a building to insulate. However, adding insulation to solid walls can lead to a significant reduction in heat loss but thought and care is needed to make sure the works are appropriate, effective and do not cause long-term problems.",02/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41208,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Solid walls
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-ceiling-level-cold-roofs/heag077-cold-roofs/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-draught-proofing-windows-doors/",,,,,,
Yf6Qw6Am,Energy Efficiency and Historic Buildings: Insulating solid ground floors,https://historicengland.org.uk/images-books/publications/eehb-insulating-solid-ground-floors/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for insulating solid masonry walls. Traditional solid wall construction is often the most difficult and in many cases the least cost effective part of a building to insulate. However, adding insulation to solid walls can lead to a significant reduction in heat loss but thought and care is needed to make sure the works are appropriate, effective and do not cause long-term problems.",03/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41209,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Thatched roofs
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-solid-ground-floors/heag087-solid-floors/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-early-cavity-walls/
",,,,,,
Sm8Ic9Ew,Energy Efficiency and Historic Buildings: Insulating solid walls,https://historicengland.org.uk/images-books/publications/eehb-insulating-solid-walls/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the methods, materials and risks involved with insulating the walls of timber-framed buildings. Making improvements can improve comfort for occupants as well as lowering fuel bills and carbon emissions. However, such improvements can raise significant technical and conservation issues.",04/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41210,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Timber-framed walls
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-solid-walls/heag081-solid-walls/
https://historicengland.org.uk/images-books/publications/eehb-secondary-glazing-windows/
https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-rafter-level-warm-roofs/
https://historicengland.org.uk/images-books/publications/eehb-insulating-timber-framed-walls/
https://historicengland.org.uk/images-books/publications/eehb-insulating-dormer-windows/",,,,,,
Kl5Tx0Ck,Energy Efficiency and Historic Buildings: Insulating thatched roofs,https://historicengland.org.uk/images-books/publications/eehb-insulating-thatched-roofs/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the methods, materials and risks involved with insulating suspended timber ground floors. The applications described are also appropriate for timber upper floors where there is an unheated space below, such as above a passageway. Advice is also provided on how suspended floors can be draught-proofed where the installation of insulation may be difficult or potentially damaging to the historic fabric of the building.",05/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41211,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Suspended timber floors
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-thatched-roofs/heag079-thatched-roofs/
https://historicengland.org.uk/images-books/publications/eehb-insulation-suspended-timber-floors/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-insulating-dormer-windows/
https://historicengland.org.uk/images-books/publications/eehb-insulating-solid-ground-floors/",,,,,,
It9Oi8Vx,Energy Efficiency and Historic Buildings: Insulating timber-framed walls,https://historicengland.org.uk/images-books/publications/eehb-insulating-timber-framed-walls/,historicengland,Historic England,eng,HTML,This guidance provides advice on how unused or intermittently used chimneys can be made more energy efficient by preventing draughts. Open chimneys and flues can be useful sources of ventilation but they can often let too much warm air out and cold air in. The resultant draughts can create uncomfortable conditions. Chimneys in older buildings can develop a wide range of defects. This guidance note also discusses how to avoid introducing further defects when measures are taken to improve energy efficiency but it does not cover the diagnosis or remedy of common defects.,06/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41212,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Open fires
Chimneys
Flues
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulating-timber-framed-walls/heag071-insultating-timber-framed-walls/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-insulation-suspended-timber-floors/
https://historicengland.org.uk/images-books/publications/eehb-open-fires-chimneys-flues/
",,,,,,
Rw5Nl5Uv,Energy Efficiency and Historic Buildings: Insulation of suspended timber floors,https://historicengland.org.uk/images-books/publications/eehb-insulation-suspended-timber-floors/,historicengland,Historic England,eng,HTML,"This guidance note provides advice on the principles, risks, materials and methods for upgrading the thermal performance of windows by the addition of secondary glazing. Older windows can often be draughty as over time they distort and gaps open up as joints become weakened. Although adequate ventilation is important in older buildings, excessive air leakage through windows is uncomfortable for occupants and wastes heat.",07/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41213,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Double glazing
Secondary glazing
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-insulation-suspended-timber-floors/heag086-suspended-timber-floors/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-secondary-glazing-windows/",,,,,,
Sa7Xe5Lk,"Energy Efficiency and Historic Buildings: Open fires, chimneys and flues",https://historicengland.org.uk/images-books/publications/eehb-open-fires-chimneys-flues/,historicengland,Historic England,eng,HTML,"The Advice Note provides:???

Advice on advice on what permissions, such as listed building consent, are needed for some of the common changes required to decarbonise and improve the energy efficiency of historic buildings?
Advice to assist local planning authorities - and other parties involved in the planning process - in determining proposals to decarbonise and improve the energy efficiency of historic buildings to enable positive climate action. Some typical building adaptations in response to climate change impacts are also included?
Signposting to other relevant information, advice, and guidance.?",08/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,41214,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Carbon Efficiency
Insulation
Energy efficiency",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-open-fires-chimneys-flues/heag080-chimneys/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-insulating-dormer-windows/",,,,,,
Ho6Yq4Hc,Energy Efficiency and Historic Buildings: Secondary glazing for windows,https://historicengland.org.uk/images-books/publications/eehb-secondary-glazing-windows/,historicengland,Historic England,eng,HTML,"These guidelines for evaluating and recording England's former gasworks and redundant gasholders are designed to inform an understanding of their significance, whilst ensuring adequate records (both above and below-ground) are made where evidence is likely to be damaged or destroyed.",09/10/2014,09/04/2021,09/04/2021,Construction companies,GB-ENG,"42990
42210",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Gasworks
Maintenance
Record keeping",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-secondary-glazing-windows/heag085-secondary-glazing/
https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/
https://historicengland.org.uk/images-books/publications/eehb-insulating-pitched-roofs-rafter-level-warm-roofs/",,,,,,
Ld5Wk1Zl,Energy Efficiency and Traditional Homes,https://historicengland.org.uk/images-books/publications/energy-efficiency-and-traditional-homes-advice-note-14/,historicengland,Historic England,eng,HTML,"This publication provides guidance to building owners, conservation professionals, local authorities and estate managers responsible for dealing with graffiti on historic buildings and sites.",10/10/2014,09/04/2021,09/04/2021,"Construction companies
Local Authorities
Building Owners",GB-ENG,"41202
41201",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Graffiti
Vandalism
Prevention
Repair",Active,,,,,,https://historicengland.org.uk/images-books/publications/adapting-historic-buildings-energy-carbon-efficiency-advice-note-18/heag321-adapting-historic-buildings-energy-carbon-efficiency/,,,,,,
Kg2Fh8Sc,Gasworks and Redundant Gasholders,https://historicengland.org.uk/images-books/publications/gasworks-and-redundant-gasholders/,historicengland,Historic England,eng,HTML,This guide has been put together to answer some of the most commonly asked questions by those who live in or care for listed buildings.,11/10/2014,09/04/2021,09/04/2021,Building Owners,GB-ENG,,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Listed Building
Maintenance
Repair",Active,,,,,,"https://historicengland.org.uk/images-books/publications/gasworks-and-redundant-gasholders/heag281-gasworks-redundant-gasholders/
https://historicengland.org.uk/images-books/publications/iha-gasworks-gasholders/
https://historicengland.org.uk/images-books/publications/dlsg-utilities-communication-structures/
https://historicengland.org.uk/images-books/publications/understanding-archaeology-of-landscapes/",,,,,,
Zk4Lj5Wi,Graffiti on Historic Buildings,https://historicengland.org.uk/images-books/publications/graffiti-on-historic-buildings/,historicengland,Historic England,eng,HTML,"The guidance is intended for wave and tidal energy developers; regulators; curators; environmental and engineering consultants; and archaeological contractors/consultants. It is intended to provide an introduction both to wave and tidal energy and to the historic environment, and to present guidance on specific issues where there is a common interest in achieving resolution. The guidance is intended to enable all parties to engage with the historic environment constructively; to help provide clarity in relation to planning; to avoid circumstances in which heritage assets become an unreasonable or unexpected constraint; and to create greater certainty for all concerned.",12/10/2014,09/04/2021,09/04/2021,"Construction companies
Environmental consultants",GB-ENG,"42910
42210
42990",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Tidal Enegy
Wave Energy
Ocean Archaeology",Active,,,,,,"https://historicengland.org.uk/images-books/publications/graffiti-on-historic-buildings/heag288-graffiti-historic-buildings/
https://historicengland.org.uk/images-books/publications/vacanthistoricbuildings/
",,,,,,
Vx4Wz3Ok,A Guide for Owners of Listed Buildings,https://historicengland.org.uk/images-books/publications/guide-for-owners-of-listed-buildings/,historicengland,Historic England,eng,HTML,"This guidance focuses on fibrous plaster ceilings, since they present a potential risk of collapse if neglected. It begins with the history of fibrous plaster, and then explains forms of deterioration, current survey standards, methods of repair and finally, management of buildings with the material.",13/10/2014,09/04/2021,09/04/2021,"Construction companies
Building owners",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Fibrous Plaster
Deterioration
Repair",Active,,,,,,"https://historicengland.org.uk/images-books/publications/guide-for-owners-of-listed-buildings/guide-for-owners-listed-buildings/
https://historicengland.org.uk/images-books/publications/listed-building-consent-advice-note-16/",,,,,,
Dt9Uq0Oz,Historic Environment Guidance for Wave and Tidal Energy,https://historicengland.org.uk/images-books/publications/historic-environment-guidance-wave-tidal-energy/,historicengland,Historic England,eng,HTML,"This note offers congregations and installers advice about Historic England's involvement with proposals to install telecommunications equipment.

It explains Historic England's role, what information we need before we can offer informed advice and the key issues about which we might be concerned.",14/10/2014,09/04/2021,09/04/2021,Places of worship,GB-ENG,43210,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Places of worship
Churches
Telecommunications
Broadband
Mobile",Active,,,,,,https://historicengland.org.uk/images-books/publications/historic-environment-guidance-wave-tidal-energy/wavetidal/,,,,,,
Ac1Ml0Wc,Historic Fibrous Plaster in the UK,https://historicengland.org.uk/images-books/publications/historic-fibrous-plaster/,historicengland,Historic England,eng,HTML,"An advisory note on underside lead corrosion.

It is intended to help professionals:

to appreciate some of the issues in their assessment of lead roofs in historic buildings.
to develop proposals for renewal or repair which can reduce the likelihood of ULC whilst minimising the amount of alterations to the buildings fabric.",15/10/2014,09/04/2021,09/04/2021,"Construction companies
Owners of historic buildings",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Lead Roofs
Maintenance
Theft Protection",Active,,,,,,https://historicengland.org.uk/images-books/publications/historic-fibrous-plaster/heag269-historic-fibrous-plaster/,,,,,,
Fo3Ti2Fx,"The Installation of Telecommunications Equipment, Including Broadband and Mobile, in Churches and Other Listed Places of Worship",https://historicengland.org.uk/images-books/publications/installation-telecomms-equip-in-places-of-worship/,historicengland,Historic England,eng,HTML,"An advisory note on underside lead corrosion.

It is intended to help professionals:

to appreciate some of the issues in their assessment of lead roofs in historic buildings.
to develop proposals for renewal or repair which can reduce the likelihood of ULC whilst minimising the amount of alterations to the buildings fabric.",16/10/2014,09/04/2021,09/04/2021,"Construction companies
Owners of historic buildings",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Lead Roofs
Maintenance
Theft Protection",Active,,,,,,"https://historicengland.org.uk/images-books/publications/installation-telecomms-equip-in-places-of-worship/installation-of-telecommunications-equip-pow-20170811/
https://historicengland.org.uk/advice/caring-for-heritage/places-of-worship/making-changes/",,,,,,
Ee2Qo6Fh,Lead roofs on historic buildings,https://historicengland.org.uk/images-books/publications/lead-roofs-on-historic-buildings/,historicengland,Historic England,eng,HTML,"An advisory note on underside lead corrosion.

It is intended to help professionals:

to appreciate some of the issues in their assessment of lead roofs in historic buildings.
to develop proposals for renewal or repair which can reduce the likelihood of ULC whilst minimising the amount of alterations to the buildings fabric.",17/10/2014,09/04/2021,09/04/2021,"Construction companies
Owners of historic buildings",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Lead Roofs
Maintenance
Theft Protection",Active,,,,,,"https://historicengland.org.uk/images-books/publications/lead-roofs-on-historic-buildings/leadroofcover-6/
https://historicengland.org.uk/images-books/publications/lead-roofs-on-historic-buildings/leadroof7-12/
https://historicengland.org.uk/images-books/publications/lead-roofs-on-historic-buildings/leadroof13-18/
https://historicengland.org.uk/images-books/publications/lead-roofs-on-historic-buildings/leadroof19-24/
",,,,,,
Cn7Rj4Me,Lightning Protection,https://historicengland.org.uk/images-books/publications/lightning-protection/,historicengland,Historic England,eng,HTML,"An advisory note on underside lead corrosion.

It is intended to help professionals:

to appreciate some of the issues in their assessment of lead roofs in historic buildings.
to develop proposals for renewal or repair which can reduce the likelihood of ULC whilst minimising the amount of alterations to the buildings fabric.",18/10/2014,09/04/2021,09/04/2021,"Construction companies
Owners of historic buildings",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Lead Roofs
Maintenance
Theft Protection",Active,,,,,,"https://historicengland.org.uk/images-books/publications/lightning-protection/heag182-lightning-protection/
https://historicengland.org.uk/images-books/publications/insuring-historic-buildings-and-other-heritage-assets/",,,,,,
Mj3Kq0Hl,Listed Building Consent,https://historicengland.org.uk/images-books/publications/listed-building-consent-advice-note-16/,historicengland,Historic England,eng,HTML,"This guidance provides advice on the design, installation and maintenance of lightning protection systems for architects, surveyors, engineers and others involved in the care of historic buildings. Lightning protection is specialist work and requires expert design and installation.",19/10/2014,09/04/2021,09/04/2021,"Architects
Engineers
Electricians",GB-ENG,43210,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Lightning Protection System
Building Protection",Active,,,,,,"https://historicengland.org.uk/images-books/publications/listed-building-consent-advice-note-16/heag304-listed-building-consent/
https://historicengland.org.uk/images-books/publications/guide-for-owners-of-listed-buildings/
https://historicengland.org.uk/images-books/publications/making-changes-heritage-assets-advice-note-2/",,,,,,
Rf3Hx6Ni,Listed Buildings and Curtilage,https://historicengland.org.uk/images-books/publications/listed-buildings-and-curtilage-advice-note-10/,historicengland,Historic England,eng,HTML,"This Historic England Advice Note gives both general advice for owners of listed buildings about listed building consent as an application process and on how to judge whether proposals need consent, how to achieve certainty on the need for consent and how to make informed applications.",20/10/2014,09/04/2021,09/04/2021,Owners of listed buildings,GB-ENG,,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Listed Building
Consent for Works",Active,,,,,,"https://historicengland.org.uk/images-books/publications/listed-buildings-and-curtilage-advice-note-10/heag125-listed-buildings-and-curtilage/
https://historicengland.org.uk/advice/planning/planning-system/",,,,,,
Na3Pj9Oa,The Maintenance and Repair of Traditional Farm Buildings,https://historicengland.org.uk/images-books/publications/maintenance-repair-trad-farm-buildings/,historicengland,Historic England,eng,HTML,This advice note gives hypothetical examples to assist in that assessment. It is based on the current legislative provision in the Planning (Listed Buildings and Conservation Areas) Act 1990 (S. 1[5]) and consideration of listed buildings and curtilage in legal cases.,21/10/2014,09/04/2021,09/04/2021,Owners of listed buildings,GB-ENG,,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Listed Building
Consent for Works
Curtilage",Active,,,,,,"https://historicengland.org.uk/images-books/publications/maintenance-repair-trad-farm-buildings/heag157-maintenance-repair-traditional-farm-buildings/
https://historicengland.org.uk/images-books/publications/adapting-traditional-farm-buildings/
https://historicengland.org.uk/images-books/publications/adaptive-reuse-traditional-farm-buildings-advice-note-9/bf
nb4rryfy",,,,,,
Cp2Uh1Kq,Making Changes to Heritage Assets,https://historicengland.org.uk/images-books/publications/making-changes-heritage-assets-advice-note-2/,historicengland,Historic England,eng,HTML,"This guidance provides practical advice to farmers, land managers and others involved with the maintenance and repair of traditional farm buildings. It also explains how work of this kind can be considered in a wider context of sustainable management to ensure these buildings have an economic value and a future.",22/10/2014,09/04/2021,09/04/2021,"Farmers
Land managers
Construction companies",GB-ENG,41201,Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Farm Buildings
Maintenance
Repairs",Active,,,,,,https://historicengland.org.uk/images-books/publications/making-changes-heritage-assets-advice-note-2/heag023-making-changes-to-heritage-assets/,,,,,,
Rf7Uy9Ee,Nanolime,https://historicengland.org.uk/images-books/publications/nanolime-use-for-consolidating-weathered-limestone/,historicengland,Historic England,eng,HTML,"This advice note illustrates the application of the policies set out in the National Planning Policy Framework in determining applications for planning permission and listed building consent, as well as other non-planning heritage consents, including scheduled monument consent.",23/10/2014,09/04/2021,09/04/2021,"Owners of heritage assets
Construction companies",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Heritage Assets
Repair
Restoration",Active,,,,,,https://historicengland.org.uk/images-books/publications/nanolime-use-for-consolidating-weathered-limestone/heag151-nanolime/,,,,,,
As5Bl6Rz,Neighbourhood Planning and the Historic Environment,https://historicengland.org.uk/images-books/publications/neighbourhood-planning-and-historic-environment-advice-note-11/,historicengland,Historic England,eng,HTML,"This guidance is aimed at conservators and those specifying conservation treatments for historic stonework. It will also be of interest to conservation officers, and building owners and managers.",24/10/2014,09/04/2021,09/04/2021,"Conservationists
Local Authorities",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Limestone
Weathering
Preservation
Nanolime",Active,,,,,,"https://historicengland.org.uk/advice/planning/improve-your-neighbourhood/neighbourhood-plan-case-studies/
https://historicengland.org.uk/advice/planning/improve-your-neighbourhood/policy-writing/
https://historicengland.org.uk/advice/planning/improve-your-neighbourhood/policy-writing/
https://historicengland.org.uk/advice/planning/improve-your-neighbourhood/neighbourhood-plan-case-studies/
https://historicengland.org.uk/advice/planning/improve-your-neighbourhood/information-sources/
",,,,,,
Gf7Vv8Fm,Planning and Archaeology,https://historicengland.org.uk/images-books/publications/planning-archaeology-advice-note-17/,historicengland,Historic England,eng,HTML,"This advice note is written to help neighbourhood planning groups, local planning authorities and other stakeholders to explore the role of historic places and local history in preparing a neighbourhood plan.",25/10/2014,09/04/2021,09/04/2021,Local Authorities,GB-ENG,"41201
41202
71112",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Planning
Historic Buildings",Active,,,,,,"https://historicengland.org.uk/images-books/publications/planning-archaeology-advice-note-17/heag314-planning-archaeology/
https://historicengland.org.uk/images-books/publications/archaeology-and-planning-case-studies/",,,,,,
Lm8Tu4Wk,Purbeck Marble,https://historicengland.org.uk/images-books/publications/purbeck-marble-conservation-repair/,historicengland,Historic England,eng,HTML,"This Historic England Advice Note describes how archaeology works in the English planning system.

Its aims are to:

summarise key responsibilities (of planning authorities and applicants) to archaeology through the planning process;
support the application of relevant legislation, national planning policy and guidance;
promote the need for rigour at key stages in the process; and
enthuse about the benefits arising from this work (including making public value apparent).",26/10/2014,09/04/2021,09/04/2021,Local Authorities,GB-ENG,"41201
41202
71112",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Planning
Historic Buildings
Archaeology",Active,,,,,,"https://historicengland.org.uk/images-books/publications/purbeck-marble-conservation-repair/heag297-purbeck-marble/
https://historicengland.org.uk/advice/technical-advice/buildings/",,,,,,
Vq7Zo2Ja,Repointing Brick and Stone Walls,https://historicengland.org.uk/images-books/publications/repointing-brick-and-stone-walls/,historicengland,Historic England,eng,HTML,"This technical advice note looks at the many complex issues that affect Purbeck Marble, the causes of decay and past interventions. It provides best practice advice for care and repair of this important stone including surveys. This guidance is intended for architects, surveyors, conservators, other conservation professionals and anyone who is interested in or responsible for the care of buildings that contain elements made of Purbeck Marble. It will aid specifiers and practitioners in making informed decisions about conserving and maintaining this type of stone.",27/10/2014,09/04/2021,09/04/2021,"Construction companies
Conservationists
Architects",GB-ENG,"41201
41202
71111",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Purbeck marble
Deterioration
Moisture
Conservation
Repair",Active,,,,,,"https://historicengland.org.uk/images-books/publications/repointing-brick-and-stone-walls/heag144-repointing-brick-and-stone-walls/
https://historicengland.org.uk/images-books/publications/conservation-basics-conservation/
https://historicengland.org.uk/images-books/publications/earth-brick-terracotta-conservation/
https://historicengland.org.uk/images-books/publications/stone-conservation/
https://historicengland.org.uk/images-books/publications/mortars-renders-plasters-conservation/",,,,,,
Eu2Bx6Bd,Sourcing Stone for Historic Building Repair,https://historicengland.org.uk/images-books/publications/sourcing-stone-for-historic-building-repair/,historicengland,Historic England,eng,HTML,"This guidance, aimed at homeowners and non-specialist building professionals, provides a brief technical guide to the key issues and stages that need to be considered when repointing brick or stone walls of older buildings.",28/10/2014,09/04/2021,09/04/2021,"Construction companies
Homeowners",GB-ENG,"41201
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Brick
Stone
Repointing
Deterioration",Active,,,,,,"https://historicengland.org.uk/advice/planning/mineral-extraction/
https://historicengland.org.uk/advice/technical-advice/buildings/building-materials-for-historic-buildings/identifying-and-sourcing-stone-for-repair/",,,,,,
Ex2Hb0Hy,Stopping the Rot,https://historicengland.org.uk/images-books/publications/stoppingtherot/,historicengland,Historic England,eng,HTML,"This Technical Advice Note is aimed at architects, surveyors, engineers, building managers, contractors, conservation officers and owners who need to obtain matching stone for repairing a historic building or monument.",29/10/2014,09/04/2021,09/04/2021,"Construction companies
Architects
Bulding owners",GB-ENG,"41201
41202
71111",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Stone Matching
Building Repair
Stone characteristics",Active,,,,,,"https://historicengland.org.uk/images-books/publications/stoppingtherot/heag046b-stopping-the-rot/
https://historicengland.org.uk/images-books/publications/stoppingtherot/heag046a-stopping-the-rot-summary/",,,,,,
Mo3Fz5Wn,"Traditional Windows: their care, repair and upgrading",https://historicengland.org.uk/images-books/publications/traditional-windows-care-repair-upgrading/,historicengland,Historic England,eng,HTML,"This guidance provides step-by-step advice on the use of the main procedures and includes case studies and a selection of specimen letters, notices, schedules and agreements. Samples of these are available to download at the bottom of this page for local authorities wishing to edit them for their own use.",30/10/2014,09/04/2021,09/04/2021,Local Authorities,GB-ENG,"41201
41202
71111",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Rot
Dryrot
Deterioration
Repair",Active,,,,,,"https://historicengland.org.uk/images-books/publications/traditional-windows-care-repair-upgrading/heag039-traditional-windows-revfeb17/
https://historicengland.org.uk/advice/technical-advice/retrofit-and-energy-efficiency-in-historic-buildings/modifying-windows-and-doors-in-historic-buildings/modifying-historic-windows-as-part-of-retrofitting-energy-saving-measures/
https://historicengland.org.uk/advice/your-home/maintain-repair/windows/
https://historicengland.org.uk/advice/technical-advice/buildings/maintenance-and-repair-of-older-buildings/",,,,,,
Oj5Xr5Zl,Waterlogged Organic Artefacts,https://historicengland.org.uk/images-books/publications/waterlogged-organic-artefacts/,historicengland,Historic England,eng,HTML,"This guidance provides step-by-step advice on the use of the main procedures and includes case studies and a selection of specimen letters, notices, schedules and agreements. Samples of these are available to download at the bottom of this page for local authorities wishing to edit them for their own use.",31/10/2014,09/04/2021,09/04/2021,Local Authorities,GB-ENG,"41201
41202
71111",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Rot
Dryrot
Deterioration
Repair",Active,,,,,,"https://historicengland.org.uk/images-books/publications/waterlogged-organic-artefacts/heag260-waterlogged-organic-artefacts/
https://historicengland.org.uk/images-books/publications/x-radiography-of-archaeological-metalwork/
https://historicengland.org.uk/images-books/publications/waterlogged-wood/
https://historicengland.org.uk/images-books/publications/environmental-archaeology-2nd/",,,,,,
Iq4Mz5Wz,Waterlogged Wood,https://historicengland.org.uk/images-books/publications/waterlogged-wood/,historicengland,Historic England,eng,HTML,"This guidance on traditional windows covers both timber and metal windows and is aimed at building professionals and property owners. Historic windows are often of considerable importance to the significance of listed buildings. They can contribute to significance through their design, materials and workmanship.",01/11/2014,09/04/2021,09/04/2021,"Construction companies
Listed property owners",GB-ENG,"41202
41201",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Windows
Timber
Metal
Listed Building Consent",Active,,,,,,"https://historicengland.org.uk/images-books/publications/waterlogged-wood/waterlogged-wood/
https://historicengland.org.uk/images-books/publications/piling-and-archaeology/
https://historicengland.org.uk/images-books/publications/environmental-archaeology-2nd/
https://historicengland.org.uk/images-books/publications/waterlogged-organic-artefacts/",,,,,,
Li2Lz2Sz,Energy Efficiency and Historic Buildings: Energy Performance Certificates (EPCs) Case Studies,https://historicengland.org.uk/images-books/publications/eehb-epcs-case-studies/,historicengland,Historic England,eng,HTML,"Waterlogged sites are usually more complex and costly to investigate than dry sites, a fact that can often put pressure on archaeological curators, contractors and consultants. It is hoped that these guidelines will help archaeologists make the best possible decisions in the face of such pressures.",02/11/2014,09/04/2021,09/04/2021,"Construction companies
Archaeologists",GB-ENG,"41202
41202",Guidance,https://historicengland.org.uk/images-books/photos/archive-services/search-and-licensing/archive-terms-and-conditions/,"Waterloggd
Wood
Preservation
Curation",Active,,,,,,"https://historicengland.org.uk/images-books/publications/eehb-epcs-case-studies/heag0307-epcs-case-studies/
https://historicengland.org.uk/services-skills/training-skills/training/webinars/recordings/previous-webinar-on-energy-performance-achieving-an-epc-b-rating/
https://historicengland.org.uk/advice/technical-advice/retrofit-and-energy-efficiency-in-historic-buildings/",,,,,,
Vf8Ns4Wq,CA 185 - Vehicle speed measurement,https://www.standardsforhighways.co.uk/search/8995b012-dac8-4ee3-a8a8-03da2e5c2ae4,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the measurement of vehicle speeds and for
determining 85th percentile speeds on existing all-purpose trunk roads.",03/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,Speed measurement,Active,,,,,,"https://www.standardsforhighways.co.uk/search/8995b012-dac8-4ee3-a8a8-03da2e5c2ae4
https://www.standardsforhighways.co.uk/search/35ffccf6-d42b-42e7-bba2-db73e5b0e83b",,,,,,
Iv4Uv9Ts,CD 109 - Highway link design,https://www.standardsforhighways.co.uk/search/c27c55b7-2dfc-4597-923a-4d1b4bd6c9fa,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for all aspects of highway link design to be
used for both new and improved all-purpose and motorway trunk roads including connector
roads.",04/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,www.nationalarchives.gov.uk/doc/open-government-licence/,"Highway link
Road design",Active,,,,,,https://www.standardsforhighways.co.uk/search/c27c55b7-2dfc-4597-923a-4d1b4bd6c9fa,,,,,,
Bq1Xp0Nm,CD 116 - Geometric design of roundabouts,https://www.standardsforhighways.co.uk/search/html/7b5ea157-9b3e-4774-9781-7d1656e83338?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides requirements for the geometric design of roundabouts.,05/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Roundabouts
Geometric design",Active,,,,,,https://www.standardsforhighways.co.uk/search/7b5ea157-9b3e-4774-9781-7d1656e83338,,,,,,
Lm0Fj4Bg,CD 122 - Geometric design of grade separated junctions,https://www.standardsforhighways.co.uk/search/3ab9ef31-9880-4e8e-a7eb-f3d218e74ffd,nationalhighways,National Highways ,eng,HTML,This document provides requirements for the geometric design of grade separated junctions.,06/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Grade sepearted junctions
Design requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/3ab9ef31-9880-4e8e-a7eb-f3d218e74ffd,,,,,,legislation.gov.uk.
Yz3Il3Fc,CD 123 - Geometric design of at-grade priority and signal-controlled junctions,https://www.standardsforhighways.co.uk/search/html/962a81c1-abda-4424-96c9-fe4c2287308c?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides requirements for the geometric design of at-grade priority and signal-controlled junctions.,07/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Priority junctions
Signal-controlled junctions
Design requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/962a81c1-abda-4424-96c9-fe4c2287308c,,,,,,
Oo9Qo5Bq,CD 127 - Cross-sections and headrooms,https://www.standardsforhighways.co.uk/search/10442706-b592-42c8-85f8-2a0c779a8e37,nationalhighways,National Highways ,eng,HTML,"This document provides requirements for the highway cross-sections and headroom at
structures for motorway and all-purpose trunk roads.",08/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highway cross-sections
Headroom
Trunk roads
Design requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/10442706-b592-42c8-85f8-2a0c779a8e37,,,,,,legislation.gov.uk.
Tc0Fw5Es,"CD 143 - Designing for walking, cycling and horse-riding",https://www.standardsforhighways.co.uk/search/9b379a8b-b2e3-4ad3-8a93-ee4ea9c03f12,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for the design of walking, cycling and
horse-riding facilities on and/or adjacent to the motorway and all-purpose trunk road network.
 ",09/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Walking
Cycling
Horse -Riding
Facility provision
Motorways
Trunk-roads",Active,,,,,,https://www.standardsforhighways.co.uk/search/9b379a8b-b2e3-4ad3-8a93-ee4ea9c03f12,,,,,,
Nn5Zh2Yy,CD 146 - Positioning of signalling and advance direction signs,https://www.standardsforhighways.co.uk/search/html/a9a33412-d92f-4ff7-87ab-daee606fa10c?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides the positioning requirements of signalling (lane signals and variable message signs) and advance direction signs for motorways,10/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Position of signalling
Lane signalling
Variable message signs
Advance direction signs",Active,,,,,,https://www.standardsforhighways.co.uk/search/a9a33412-d92f-4ff7-87ab-daee606fa10c,,,,,,
Ep6Kq6Ie,"CD 169 - The design of lay-bys, maintenance hardstandings, rest areas, service areas and observation platforms",https://www.standardsforhighways.co.uk/search/d0c173e3-7a75-4bce-b535-1c11d3b90b61,nationalhighways,National Highways ,eng,HTML,"This document gives the requirements and provides advice for the location and layout of lay-bys
(including parking lay-bys, bus lay-bys and emergency lay-bys), maintenance hardstandings,
rest areas, service areas and observation platforms.
",11/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Lay-bys
Rest areas
Trunk road service areas
observation platforms",Active,,,,,,https://www.standardsforhighways.co.uk/search/d0c173e3-7a75-4bce-b535-1c11d3b90b61,,,,,,
Ls1As3Nj,CD 192 - The design of crossovers and changeovers,https://www.standardsforhighways.co.uk/search/2a0b909d-d8e8-4178-a473-74b35f2b30a0,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the design of crossovers and changeovers,12/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Crossovers
Geometric design
Changeovers",Active,,,,,,https://www.standardsforhighways.co.uk/search/2a0b909d-d8e8-4178-a473-74b35f2b30a0,,,,,,legislation.gov.uk.
Db0Fp2Kt,CD 193 - Driver location signs,https://www.standardsforhighways.co.uk/search/3a8e4a48-56f9-4165-845e-aab8b566c17d,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the design and implementation of driver location
signs (DLS) for motorways and all-purpose trunk roads.",13/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Driver location signs,Active,,,,,,https://www.standardsforhighways.co.uk/search/3a8e4a48-56f9-4165-845e-aab8b566c17d,,,,,,legislation.gov.uk.
Ud2Hk3Zp,CD 195 - Designing for cycle traffic,https://www.standardsforhighways.co.uk/search/4b59ebc3-065b-467f-8b43-09d2802f91c8,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for cycle traffic on the trunk road and motorway
network.",14/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Cyclists
Cycle traffic",Active,,,,,,https://www.standardsforhighways.co.uk/search/4b59ebc3-065b-467f-8b43-09d2802f91c8,,,,,,legislation.gov.uk.
Ps0Ln3Is,CD 224 - Traffic assessment,https://www.standardsforhighways.co.uk/search/257e5888-2bfd-492d-92d4-ecf7d40428b0,nationalhighways,National Highways ,eng,HTML,"This document sets out the method for calculating traffic loading for the design of road
pavements.",15/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Calculation of design traffic
Growth factor
Wear factor",Active,,,,,,https://www.standardsforhighways.co.uk/search/257e5888-2bfd-492d-92d4-ecf7d40428b0,,,,,,
Xu6Yo3Dc,CD 225 - Design for new pavement foundations,https://www.standardsforhighways.co.uk/search/0d63993a-89f1-4312-bd71-d3b019a32810,nationalhighways,National Highways ,eng,HTML,"This document sets out the design procedure for pavement foundations in terms of the ability of
the foundation to resist loads applied both during construction and the service life of the
pavement.",16/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road drainage layers
Road foundation design
Load resistance",Active,,,,,,https://www.standardsforhighways.co.uk/search/0d63993a-89f1-4312-bd71-d3b019a32810,,,,,,
Dq5Fy0Nz,CD 226 - Design for new pavement construction,https://www.standardsforhighways.co.uk/search/9654b4de-efa7-4843-8598-295019387077,nationalhighways,National Highways ,eng,HTML,"This document gives the requirements for the design of pavement construction for new build
carriageways, widening of existing carriageways, or reconstruction of existing pavements on the
UK motorway and all-purpose trunk road network.",17/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Pavement design
Pavement upgrade
Cold recycled base materials
Alternative design procedures",Active,,,,,,https://www.standardsforhighways.co.uk/search/9654b4de-efa7-4843-8598-295019387077,,,,,,
Xh7Ts7Wj,CD 227 - Design for pavement maintenance,https://www.standardsforhighways.co.uk/search/0ff37fc4-9db6-495a-9460-843a55c0fc0c,nationalhighways,National Highways ,eng,HTML,"This document describes the requirements to determine the need for maintenance and to design
pavement renewals maintenance treatments on the UK motorway and all-purpose trunk roads.",18/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Investigation plan
Origin of defects
Maintenance
Pavement deterioration
Retexturing
Flexible pavements
Rigid pavements",Active,,,,,,https://www.standardsforhighways.co.uk/search/0ff37fc4-9db6-495a-9460-843a55c0fc0c,,,,,,
Ay0Ni4Kk,CD 236 - Surface course materials for construction,https://www.standardsforhighways.co.uk/search/html/815f3a3c-efe5-4555-9003-9ee38c2d080b?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides requirements for pavement surfacing for both flexible and rigid pavements,19/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Aggregate selection
Surface course material",Active,,,,,,https://www.standardsforhighways.co.uk/search/815f3a3c-efe5-4555-9003-9ee38c2d080b,,,,,,
Ql8Jd5Wz,CD 239 - Footway and cycleway pavement design,https://www.standardsforhighways.co.uk/search/313250ad-268f-45fd-9446-aae6ad8c4e54,nationalhighways,National Highways ,eng,HTML,This document provides requirements for pavement surfacing for both flexible and rigid pavements,20/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Pavement design
Cycleway design
Geometry
Drainage",Active,,,,,,https://www.standardsforhighways.co.uk/search/313250ad-268f-45fd-9446-aae6ad8c4e54,,,,,,
Gb9Me7Op,CD 350 - The design of highway structures,https://www.standardsforhighways.co.uk/search/19858eae-6dd2-4669-90a7-38aa8c85a1dd,nationalhighways,National Highways ,eng,HTML,"This document contains requirements, advice and guidance of the Overseeing Organisation for the design of highway structures.",21/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Design requirmeents
Durability
Reporting requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/19858eae-6dd2-4669-90a7-38aa8c85a1dd,,,,,,
Xk2Qj0Oo,CD 351 - The design and appearance of highway structures,https://www.standardsforhighways.co.uk/search/1ae4cbff-c144-4930-a223-e76d17253e26,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and guidance which aim to improve the aesthetic
outcomes of schemes that include bridges and other highway structures.",22/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Aesthetic appraisal
Bridges
Aesthetics Stakeholders",Active,,,,,,https://www.standardsforhighways.co.uk/search/1ae4cbff-c144-4930-a223-e76d17253e26,,,,,,
Aj7Kn3Zr,CD 352 - Design of road tunnels,https://www.standardsforhighways.co.uk/search/987a669b-13a1-40b9-94da-1ea4e4604fdd,nationalhighways,National Highways ,eng,HTML,"This document describes the procedures necessary for the design and refurbishment of all
tunnels on the motorway and all-purpose trunk road network.",23/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Planning
Safety
General Design
Road Tunnel Safety
Geometric design
Ventilation requirements
Lighting design
Drainage system
Fire engineering
Traffic control
Power supply
Plant monitoring",Active,,,,,,https://www.standardsforhighways.co.uk/search/987a669b-13a1-40b9-94da-1ea4e4604fdd,,,,,,
Eg5Mh8Rc,CD 353 - Design criteria for footbridges,https://www.standardsforhighways.co.uk/search/7be571c3-bcd5-414c-b608-48aa19f7f4a1,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the design criteria for footbridges.,24/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Design standards
Dimensional standards
Parapets
Enclosed footbridges
Drainage
Walkway surface",Active,,,,,,https://www.standardsforhighways.co.uk/search/7be571c3-bcd5-414c-b608-48aa19f7f4a1,,,,,,
Kz5Jg7Uo,CD 354 - Design of minor structures,https://www.standardsforhighways.co.uk/search/a305f35f-2ec3-4e68-b4ca-e252af061249,nationalhighways,National Highways ,eng,HTML,"This document covers the design of minor highway structures including lighting columns,
cantilever masts for traffic signals and/or speed cameras, CCTV masts, and fixed vertical road
traffic signs. It incorporates the provisions of BS EN 40, BS EN 12899 and supersedes BD 94/17.",25/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Dimensional limitations
Design criteria
Use of British Standards
Lighting columns
Flange plates
Steel structures",Not active,,,,,,https://www.standardsforhighways.co.uk/search/d3263218-52b9-48ae-b5a9-2250f17ed613,,,,,,
Po7Is8Jn,CD 355 - Application of whole-life costs for design and maintenance of highway structures,https://www.standardsforhighways.co.uk/search/fc593d16-caf3-41b1-9950-ae8cc974f577,nationalhighways,National Highways ,eng,HTML,"This document covers the application of the whole life costs analysis at the design development
stage of new structures and the design of maintenance interventions.",26/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Evaluation procedure
Traffic delay costs
Life-cycle plan",Active,,,,,,https://www.standardsforhighways.co.uk/search/fc593d16-caf3-41b1-9950-ae8cc974f577,,,,,,
Ai8Ar2Ax,CD 356 - Design of highway structures for hydraulic action,https://www.standardsforhighways.co.uk/search/559b43dc-82db-46c9-be1a-f2b718e8db62,nationalhighways,National Highways ,eng,HTML,"This document provides information on the hydraulic aspects of the design of structures in or over
rivers, estuaries and flood plains, including the studies required to support these design aspects.",27/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Scour protection
Hydraulic action
Erosion",Active,,,,,,https://www.standardsforhighways.co.uk/search/559b43dc-82db-46c9-be1a-f2b718e8db62,,,,,,
Jw0Pe9Ge,CD 357 - Bridge expansion joints,https://www.standardsforhighways.co.uk/search/038b8726-2014-4ec9-ae2c-0043b97bd05c,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for the design and specification of expansion joints for
use in highway bridge decks. It also provides supporting advice on the selection, installation,
management and maintenance of various types of expansion joints.",28/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Joint type selection
Joint design requirmeents
Expansion joint
Joint installation",Active,,,,,,https://www.standardsforhighways.co.uk/search/038b8726-2014-4ec9-ae2c-0043b97bd05c,,,,,,
Fc1Qs7Lf,CD 358 - Waterproofing and surfacing of concrete bridge decks,https://www.standardsforhighways.co.uk/search/html/d618f15c-5fd3-4802-a986-aaa0581c98fa?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"This document gives the requirements for the design, materials and workmanship for the waterproofing and surfacing of concrete bridge decks. Waterproofing and surfacing of concrete bridge decks",29/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Drainage
Water Management
Concrete deck
Waterproofing
Carriageways
Footways",Active,,,,,,https://www.standardsforhighways.co.uk/search/d618f15c-5fd3-4802-a986-aaa0581c98fa,,,,,,
Kn0Qq5Af,CD 359 - Design requirements for permanent soffit formwork,https://www.standardsforhighways.co.uk/search/64b30345-4a21-4552-83ce-2f832244f1f6,nationalhighways,National Highways ,eng,HTML,This document sets out design requirements for permanent soffit formwork for bridges.,30/11/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Formwork
Design requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/64b30345-4a21-4552-83ce-2f832244f1f6,,,,,,
Fo6Cj9Rs,CD 360 - Use of compressive membrane action in bridge decks,https://www.standardsforhighways.co.uk/search/7cc0c494-2a45-42c8-b12d-f4c7bdad04c3,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for the use of compressive membrane action
in the design and assessment of reinforced concrete bridge deck slabs.",01/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Membranes
Limit state
Local capacity of bridge deck slabs",Active,,,,,,https://www.standardsforhighways.co.uk/search/7cc0c494-2a45-42c8-b12d-f4c7bdad04c3,,,,,,
Pu2Tx5Zv,CD 361 - Weathering steel for highway structures,https://www.standardsforhighways.co.uk/search/448ff213-9b93-439d-92de-0194a52f7644,nationalhighways,National Highways ,eng,HTML,This document provides requirements for use of weathering steel in highway structures.,02/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Weathering steel
Limitations on use
Structure records
Environmental classification",Active,,,,,,https://www.standardsforhighways.co.uk/search/448ff213-9b93-439d-92de-0194a52f7644,,,,,,
Tb7Cb9Mr,CD 362 - Enclosure of bridges,https://www.standardsforhighways.co.uk/search/db186d41-a36f-4e63-b312-a30f7bd88e85,nationalhighways,National Highways ,eng,HTML,"This document describes the requirements for the implementation of an enclosure as a means of
bridge protection. This document gives the methods of evaluating and the design requirements.",03/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Performance criteria
Bridges
Enclosure materials",Active,,,,,,https://www.standardsforhighways.co.uk/search/db186d41-a36f-4e63-b312-a30f7bd88e85,,,,,,
Kw6Fu7Pi,CD 363 - Design rules for aerodynamic effects on bridges,https://www.standardsforhighways.co.uk/search/1f5ff91d-f087-46a6-b418-aa2b64ad4b45,nationalhighways,National Highways ,eng,HTML,"This document sets out the design requirements for bridges with respect to aerodynamic effects
including provisions for wind-tunnel testing. It updates and supersedes BD 49/01.",04/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Aerodynamic stabilty
Bridges
Load factors
Wind tunnel testing",Active,,,,,,https://www.standardsforhighways.co.uk/search/1f5ff91d-f087-46a6-b418-aa2b64ad4b45,,,,,,
Ka8Gi5Dy,CD 364 - Formation of continuity joints in bridge decks,https://www.standardsforhighways.co.uk/search/6b0e068c-12f4-4dbe-95e3-bc3100ec8e66,nationalhighways,National Highways ,eng,HTML,"This document provides information on the design of continuity joints in trafficked concrete
bridge decks for the effects of early age vibration and differential deflection of the decks.",05/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Bridges
Bridge deck
Deck widening",Active,,,,,,https://www.standardsforhighways.co.uk/search/6b0e068c-12f4-4dbe-95e3-bc3100ec8e66,,,,,,
Jr3St5Vh,CD 365 - Portal and cantilever signs/signals gantries,https://www.standardsforhighways.co.uk/search/6df58b73-a71f-48dc-8b76-b073220c8702,nationalhighways,National Highways ,eng,HTML,"This document covers the design of portal and cantilever sign and signal gantries to Eurocodes
and sets out the Overseeing Organisation's requirements",06/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Signal gantries
Cantilevel signs
Portal signs
Gantry type
Aesthetics
Cabling",Active,,,,,,https://www.standardsforhighways.co.uk/search/6df58b73-a71f-48dc-8b76-b073220c8702,,,,,,
Nx7Dr8Qn,CD 366 - Design criteria for collision protection beams,https://www.standardsforhighways.co.uk/search/19b2054b-9bb5-4883-96c0-5c02c1e20e32,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the design of beams protecting existing structures
from serious damage due to bridge strikes by over-height vehicles.",07/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Collision protection beams
Design
Installation",Active,,,,,,https://www.standardsforhighways.co.uk/search/19b2054b-9bb5-4883-96c0-5c02c1e20e32,,,,,,
Sn5Hu3Bc,CD 367 - Treatment of existing structures on highways widening schemes,https://www.standardsforhighways.co.uk/search/950672b0-feee-4036-b0a5-9d1830bbdd36,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements and advice for the treatment of structures on highway
widening schemes on motorways and all-purpose trunk roads, and setting out the principles to
be applied in the process.",08/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Existing structues
Widening
Motorways",Active,,,,,,https://www.standardsforhighways.co.uk/search/950672b0-feee-4036-b0a5-9d1830bbdd36,,,,,,
Xs3Qp8Wq,CD 368 - Design of fibre reinforced polymer bridges and highway structures,https://www.standardsforhighways.co.uk/search/4075e21b-fd36-4479-a620-9941370aa3f8,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the design of fibre reinforced polymer bridges.,09/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Bridges
Fibre reinforced polymer
Testing
FRP Bridges",Active,,,,,,https://www.standardsforhighways.co.uk/search/4075e21b-fd36-4479-a620-9941370aa3f8,,,,,,
Ph7Gy2Wt,CD 369 - Surface protection for concrete highway structures,https://www.standardsforhighways.co.uk/search/a60422de-22ff-4449-97fb-cc2ebabecaa9,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements and supporting advice for the surface protection for
concrete highway structures.",10/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Surface protection
Anti-graffiti
Anti-carbonation
Materials",Active,,,,,,https://www.standardsforhighways.co.uk/search/a60422de-22ff-4449-97fb-cc2ebabecaa9,,,,,,
Dq2Iz1Hg,CD 370 - Cathodic protection for use in reinforced concrete highway structures,https://www.standardsforhighways.co.uk/search/c937b97a-3ccf-4f55-ab25-f8dd21aa883c,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for the design of cathodic protection to
stop/halt corrosion of reinforcement in highway structures.",11/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highway structures
Cathodic protection
Monitoring",Active,,,,,,https://www.standardsforhighways.co.uk/search/c937b97a-3ccf-4f55-ab25-f8dd21aa883c,,,,,,
Si2Ja7Kg,CD 371 - Strengthening highway structures using fibre-reinforced polymers and externally bonded steel plates,https://www.standardsforhighways.co.uk/search/34bd12c5-5840-404f-8093-bd39639fe569,nationalhighways,National Highways ,eng,HTML,"The use of this document enables existing concrete and steel highway structures to be
strengthened using fibre-reinforced polymers (FRPs) or externally bonded steel plates, thereby
reducing risk and maintaining a safe and operational network.",12/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Fibre-reinforced polymers
Externally bonded steel plates
Concrete bridge decks
Concrete bridge supports
Strengthening",Active,,,,,,https://www.standardsforhighways.co.uk/search/34bd12c5-5840-404f-8093-bd39639fe569,,,,,,
Qs9Fs4Ot,CD 372 - Design of post-installed anchors and reinforcing bar connections in concrete,https://www.standardsforhighways.co.uk/search/87e6d306-b757-4cd8-9879-05cf4c1d7894,nationalhighways,National Highways ,eng,HTML,"This document provides design requirements for post-installed anchors and reinforcing bar
connections - collectively referred to as fixings - in concrete, including the conceptual design and
detailed design requirements for both new and existing structures.
",13/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Anchors
Reinforcing bar
Post-installed fixings
Fire",Active,,,,,,https://www.standardsforhighways.co.uk/search/87e6d306-b757-4cd8-9879-05cf4c1d7894,,,,,,
Sq2Ar6Dk,CD 373 - Impregnation of reinforced and prestressed concrete highway structures using hydrophobic pore-lining impregnants,https://www.standardsforhighways.co.uk/search/3963f0e7-fead-4993-851d-eaef743e7b9f,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the application of hydrophobic impregnation
providing protection to concrete highway structures.",14/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Impregnation systems
Hydrophobic impregnation",Active,,,,,,https://www.standardsforhighways.co.uk/search/3963f0e7-fead-4993-851d-eaef743e7b9f,,,,,,
Bz5Ja6Oi,CD 374 - The use of recycled aggregates in structural concrete,https://www.standardsforhighways.co.uk/search/e0ba4369-b995-4aff-8aa3-f57b69b3928d  ,nationalhighways,National Highways ,eng,HTML,"This document enables the use of recycled aggregates in structural concrete for highways
structures, providing key information that is required to design structural concrete containing
recycled aggregates and manage the risks in their adoption.",15/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Recycled aggregate
Structural concrete
Degradation",Active,,,,,,https://www.standardsforhighways.co.uk/search/e0ba4369-b995-4aff-8aa3-f57b69b3928d,,,,,,
Uo3Xo0Kx,CD 375 - Design of corrugated steel buried structures,https://www.standardsforhighways.co.uk/search/9fb3e066-2afc-457e-a744-cb488e8d567f,nationalhighways,National Highways ,eng,HTML,"This document details the design requirements for corrugated steel buried structures that act
compositely with the surrounding material to resist loading",16/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Design principles
Compressive hoop
Structural resistance
Corrugated steel
Buried structures",Active,,,,,,https://www.standardsforhighways.co.uk/search/9fb3e066-2afc-457e-a744-cb488e8d567f,,,,,,
Vg0Yo0Yu,CD 376 - Unreinforced masonry arch bridges,https://www.standardsforhighways.co.uk/search/60408791-605b-45d7-980b-dfc570ee60f3,nationalhighways,National Highways ,eng,HTML,This document covers the design of new unreinforced masonry arch bridges.,17/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Masonry arch bridges
Arch ring
Parapets
Spandrel walls",Active,,,,,,https://www.standardsforhighways.co.uk/search/60408791-605b-45d7-980b-dfc570ee60f3,,,,,,
Ke0Dk7Vw,CD 377 - Requirements for road restraint systems,https://www.standardsforhighways.co.uk/search/1fe48581-82ba-4b6f-95a1-ee93309bd1b5,nationalhighways,National Highways ,eng,HTML,"This document details the requirements for permanent and temporary safety barriers, vehicle
parapets, terminals, transitions, crash cushions, pedestrian parapets, pedestrian guardrails and
pedestrian restraint and protection, vehicle arrester beds, anti-glare systems and cattle grids.",18/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road restrain systems
Permanent safety barriers
Vehicle parapets
Terminals
Transitions
Crash cushions
Pedestrian restraints
Temporary safety barriers",Active,,,,,,https://www.standardsforhighways.co.uk/search/1fe48581-82ba-4b6f-95a1-ee93309bd1b5,,,,,,
Mr4Xl7Rh,CD 378 - Impact test and assessment criteria for truck mounted attenuators,https://www.standardsforhighways.co.uk/search/6e2e1dab-2d7c-4ceb-b217-fe3bf8b3afe0,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the testing and assessment of truck mounted
attenuators (formerly known as lorry-mounted crash cushions (LMCCs)).",19/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Impact test
Truck mounted attenuators
Parameters
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/6e2e1dab-2d7c-4ceb-b217-fe3bf8b3afe0,,,,,,
Fz9Wu3Yj,CD 521 - Hydraulic design of road edge surface water channels and outlets,https://www.standardsforhighways.co.uk/search/html/040d234a-e995-4776-a269-9dafef538237?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"This document gives requirements and guidance for the design of road edge surface water channels and outlets, combined channel and pipe systems for surface water drainage, and grassed surface water channels on motorways and all-purpose trunk roads.",20/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Surface water channel systems
Water outlets
Road edge",Active,,,,,,https://www.standardsforhighways.co.uk/search/040d234a-e995-4776-a269-9dafef538237,,,,,,
Rd8Tz0Hf,CD 522 - Drainage of runoff from natural catchments,https://www.standardsforhighways.co.uk/search/09c28187-371e-4180-8373-939f48607c01,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for dealing with surface water runoff from
natural catchments draining towards motorways or all-purpose trunk roads, in order to limit the
frequency and severity of flooding incidents caused by runoff from beyond the highway boundary.",21/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Drainage
Runoff
Natural Catchments",Active,,,,,,https://www.standardsforhighways.co.uk/search/09c28187-371e-4180-8373-939f48607c01,,,,,,
Bg9Nt3Eq,CD 523 - Determination of pipe roughness and assessment of sediment deposition to aid pipeline design,https://www.standardsforhighways.co.uk/search/b8f7eed8-69d9-4016-be2a-860404191f3c,nationalhighways,National Highways ,eng,HTML,"This document sets out the optimum design of highway drainage pipelines, based on sediment
transport, in terms of roughness coefficient and velocity. It provides an assessment of the
volume of sediment deposition that can occur in proposed and existing pipelines.",22/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Pipeline
Pipe roughness
Sediment transport
Sediment deposition",Active,,,,,,https://www.standardsforhighways.co.uk/search/b8f7eed8-69d9-4016-be2a-860404191f3c,,,,,,
Ay8Ta9Va,CD 524 - Edge of pavement details,https://www.standardsforhighways.co.uk/search/html/76d9df3c-255b-4d48-87c8-6f30a1ba4a6d?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides guidance on the use of the various types of edge of pavement drainage details which are depicted in the 'B' and 'F' series of the Highway Construction Details (HCD): Manual of Contract Documents for Highway Works (MCHW3).,23/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Surface and sub-surface drains
Water channels
Drainage channel
Edge of pavement",Active,,,,,,https://www.standardsforhighways.co.uk/search/76d9df3c-255b-4d48-87c8-6f30a1ba4a6d,,,,,,
Ws9Lm6In,CD 525 - Design of combined surface and sub-surface drains and management of stone scatter,https://www.standardsforhighways.co.uk/search/cf18fb19-ce74-4c07-9940-945c7fca4962,nationalhighways,National Highways ,eng,HTML,"This document sets out requirements and provides recommendations on the design of new
combined surface and sub-surface drains (also called French drains), and the treatment of
existing combined surface and sub-surface drains where used as a road drainage system.",24/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Surface and sub-surface drains
Stone scatter
Vehicle stranding",Active,,,,,,https://www.standardsforhighways.co.uk/search/cf18fb19-ce74-4c07-9940-945c7fca4962,,,,,,
Uj7Jx7Fv,CD 526 - Spacing of road gullies,https://www.standardsforhighways.co.uk/search/a869ed8e-4470-4286-aef4-7d11af24a597,nationalhighways,National Highways ,eng,HTML,"This document provides the requirements and advice for determining the length of road that can
be drained by grating and kerb outlets.",25/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road gullies
Gully grating
Kerb inlets
Hydraulic design",Active,,,,,,https://www.standardsforhighways.co.uk/search/a869ed8e-4470-4286-aef4-7d11af24a597,,,,,,
Jf6Lm4Ep,CD 527 - Sumpless gullies,https://www.standardsforhighways.co.uk/search/6b21ffb1-e7f4-498d-8750-0fb4e7d7425c,nationalhighways,National Highways ,eng,HTML,This document provides the requirements and advice for the design of sumpless gullies.,26/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Sumpless gullies,Active,,,,,,https://www.standardsforhighways.co.uk/search/6b21ffb1-e7f4-498d-8750-0fb4e7d7425c,,,,,,
Pi8Tk4Op,CD 528 - Vortex separators for use with road drainage systems,https://www.standardsforhighways.co.uk/search/0e30bf41-c55a-43ec-8b7f-1dac49d81d20,nationalhighways,National Highways ,eng,HTML,"This document provides the requirements and advice for including vortex separators within road
drainage systems.",27/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Vortex seperators
Highways design
Design requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/0e30bf41-c55a-43ec-8b7f-1dac49d81d20,,,,,,
Ft4Vd5Lq,CD 529 - Design of outfall and culvert details,https://www.standardsforhighways.co.uk/search/html/ad5be9a5-e318-4896-9163-90f118b6799d?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the design of outfall and culvert details.,28/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Outfalls
Culverts",Active,,,,,,https://www.standardsforhighways.co.uk/search/ad5be9a5-e318-4896-9163-90f118b6799d,,,,,,
Fc4Le0Zj,CD 530 - Design of soakaways,https://www.standardsforhighways.co.uk/search/html/35cc265d-16be-4b8c-9cd4-77fdbd8487a2?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides requirements for and advice on the design of soakaways that can be incorporated into systems used to treat and store road runoff prior to discharging to ground.,29/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Soakaway systems",Active,,,,,,https://www.standardsforhighways.co.uk/search/35cc265d-16be-4b8c-9cd4-77fdbd8487a2,,,,,,
Ma3Wt0Sw,CD 531 - Reservoir pavements for drainage attenuation,https://www.standardsforhighways.co.uk/search/html/85de273e-ebe1-433e-83ba-a7f8d2b714a8?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document provides requirements and guidance for the design of reservoir pavements to be used on motorway and all-purpose trunk roads.,30/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Reservoir pavements",Active,,,,,,https://www.standardsforhighways.co.uk/search/85de273e-ebe1-433e-83ba-a7f8d2b714a8,,,,,,
Ik4Qj1Zd,CD 532 - Vegetated drainage systems for highway runoff,https://www.standardsforhighways.co.uk/search/cfba97e7-5c58-4b50-ac54-c4d2a2bfe363,nationalhighways,National Highways ,eng,HTML,"This document gives the requirements and advice for the design of vegetated drainage systems
to convey, store and treat runoff from motorways and all-purpose trunk roads.",31/12/2014,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Vegetated drainage systems
Runoff",Active,,,,,,https://www.standardsforhighways.co.uk/search/cfba97e7-5c58-4b50-ac54-c4d2a2bfe363,,,,,,
Yo0Sa1St,CD 533 - Determination of pipe and bedding combinations for drainage works,https://www.standardsforhighways.co.uk/search/html/a9226466-0852-4230-b306-4568cf8d4985?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains requirements and guidance for selecting suitable combinations of drainage pipes and bedding types to meet given loading requirements.,01/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Pipe and bedding
Drainage",Active,,,,,,https://www.standardsforhighways.co.uk/search/a9226466-0852-4230-b306-4568cf8d4985,,,,,,
Li8Pv2Jy,CD 534 - Chamber tops and gully tops for road drainage and services,https://www.standardsforhighways.co.uk/search/d2d4a620-bb06-488f-b642-4fe16a192ccf,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for road chamber top and gully top installations on
motorway and all-purpose trunk roads.",02/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Chamber tops
Gully tops",Active,,,,,,https://www.standardsforhighways.co.uk/search/d2d4a620-bb06-488f-b642-4fe16a192ccf,,,,,,
Xz5Mb7Bg,CD 535 - Drainage asset data and risk management,https://www.standardsforhighways.co.uk/search/e0b6eaa6-b5ec-4e3f-a54f-93bd20fdf5db,nationalhighways,National Highways ,eng,HTML,"This document defines the requirements for recording of inventory and condition of drainage
assets, and the management of flooding, pollution and cross-asset risks related to drainage.",03/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Asset data
Flood risk
Water quality",Active,,,,,,https://www.standardsforhighways.co.uk/search/e0b6eaa6-b5ec-4e3f-a54f-93bd20fdf5db,,,,,,
Hs8Dl6Of,CD 622 - Managing geotechnical risk,https://www.standardsforhighways.co.uk/search/ff5ed991-71ed-4ff2-9800-094e18cd1c4c,nationalhighways,National Highways ,eng,HTML,"This document defines the technical approval and certification procedures to be used to ensure
that the risks associated with geotechnical activities are appropriately managed.",04/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Geotechnical risk
Risks",Active,,,,,,https://www.standardsforhighways.co.uk/search/ff5ed991-71ed-4ff2-9800-094e18cd1c4c,,,,,,
Ir9Mc4Nd,CG 152 - Traffic signs to tourist destinations and leisure facilities,https://www.standardsforhighways.co.uk/search/d7a5a572-3661-413b-84b0-c2c4efecb50d,nationalhighways,National Highways ,eng,HTML,This document provides requirements and advice for the provision of tourist and leisure signs.,05/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road signs
Tourists
Leisure facilities",Active,,,,,,https://www.standardsforhighways.co.uk/search/d7a5a572-3661-413b-84b0-c2c4efecb50d,,,,,,
Za7Dd8Cq,CG 153 - Traffic signs to retail destinations and exhibition centres,https://www.standardsforhighways.co.uk/search/17db15b9-f159-41ca-8420-0f25cc38ccfd,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for traffic signs to retail destinations and exhibition
centres.",06/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Retail destination
Exhibition centre",Active,,,,,,https://www.standardsforhighways.co.uk/search/17db15b9-f159-41ca-8420-0f25cc38ccfd,,,,,,
Sc1Wl4Uk,CG 300 - Technical approval of highway structures,https://www.standardsforhighways.co.uk/search/17dadcc6-8e01-455d-b93e-c827d280839a,nationalhighways,National Highways ,eng,HTML,"Construction (Design and Management) Regulations 2015 *Added provisions for structures
options reports",07/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Approval requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/17dadcc6-8e01-455d-b93e-c827d280839a,,,,,,
Qw5Cj3Mc,"CG 302 - As-built, operational and maintenance records for highway structures",https://www.standardsforhighways.co.uk/search/6743aabd-d2e3-466b-a480-7643ccb6dcbd,nationalhighways,National Highways ,eng,HTML,"This document gives the Overseeing Organisations' minimum requirements for the records to be
collected and maintained for highway structures.",08/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Record keeping",Active,,,,,,https://www.standardsforhighways.co.uk/search/6743aabd-d2e3-466b-a480-7643ccb6dcbd,,,,,,
Jq1Os0Kf,CG 303 - Quality assurance scheme for paints and similar protective coatings,https://www.standardsforhighways.co.uk/search/10e366ec-8fd7-4891-a796-bcc0c02fb866,nationalhighways,National Highways ,eng,HTML,"This document gives details of the quality assurance scheme for paints and similar protective
coatings that are used to protect steelwork in highway structures against corrosion.",09/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Quality assurance scheme
Paint
Certification",Active,,,,,,https://www.standardsforhighways.co.uk/search/10e366ec-8fd7-4891-a796-bcc0c02fb866,,,,,,
Xs7Yj6Fw,CG 304 - Conservation of highway structures,https://www.standardsforhighways.co.uk/search/d174016a-81d2-469b-b1d7-ca84ec2fb815,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the conservation of highway structures.,10/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Conservation
Listed buildings
Scheduled monuments",Active,,,,,,https://www.standardsforhighways.co.uk/search/d174016a-81d2-469b-b1d7-ca84ec2fb815,,,,,,
Gv6Qq5Dp,CG 305 - Identification marking of highway structures,https://www.standardsforhighways.co.uk/search/80f6705d-a55b-4597-8a06-a931c47113d5,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for identification marking of highway structures on
motorways and all-purpose trunk roads, including overbridges and underbridges.",11/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Identification markers
Painting
Siting of markers",Active,,,,,,https://www.standardsforhighways.co.uk/search/80f6705d-a55b-4597-8a06-a931c47113d5,,,,,,
Pl2Xt7Ej,CG 501 - Design of highway drainage systems,https://www.standardsforhighways.co.uk/search/html/6355ee38-413a-4a11-989b-0f33af89c4ed?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the over-arching requirements for drainage design on highways.,12/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Drainage
Climate change
Flood risk
Pollution",Active,,,,,,https://www.standardsforhighways.co.uk/search/6355ee38-413a-4a11-989b-0f33af89c4ed,,,,,,
Kv0Rm6Zp,CG 502 - The certification of drainage design,https://www.standardsforhighways.co.uk/search/23963b9e-3f56-4c5a-9496-afab54d289d0,nationalhighways,National Highways ,eng,HTML,"This document outlines the requirements for the certification of drainage design on motorway
and all-purpose trunk roads.",13/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Drainage
Certification",Active,,,,,,https://www.standardsforhighways.co.uk/search/23963b9e-3f56-4c5a-9496-afab54d289d0,,,,,,
Tj2Tv7Ci,CM 125 - Maintenance of traffic signs,https://www.standardsforhighways.co.uk/search/6202476d-c352-4e08-8ddf-0c7de9155a43,nationalhighways,National Highways ,eng,HTML,This document sets out the requirements for the maintenance of permanent traffic signs.,14/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Signage
Manitenance
Defects",Active,,,,,,https://www.standardsforhighways.co.uk/search/6202476d-c352-4e08-8ddf-0c7de9155a43,,,,,,
Ua3Jt8Jd,CM 231 - Pavement surface repairs,https://www.standardsforhighways.co.uk/search/df52250c-a3c3-4d8a-b55a-c418e82ad243,nationalhighways,National Highways ,eng,HTML,"This document provides guidance on methods to be used for minor repairs of both flexible and
rigid pavements.",15/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Pavement surface
Crack repairs
Bitumen
Concrete",Active,,,,,,https://www.standardsforhighways.co.uk/search/df52250c-a3c3-4d8a-b55a-c418e82ad243,,,,,,
Tb8Yp6Fe,CM 430 - Maintenance of road tunnels,https://www.standardsforhighways.co.uk/search/1ca0d3ec-7157-4d5f-b051-d63eccb45db2,nationalhighways,National Highways ,eng,HTML,"This document describes procedures for the safe and effective maintenance of tunnels on the
motorway and all-purpose trunk road network.",16/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road tunnels
Maintenance
Cleaning
Inspections
Ventilation
Lighting
Drainage
Fire safety
Emergency planning",Active,,,,,,https://www.standardsforhighways.co.uk/search/1ca0d3ec-7157-4d5f-b051-d63eccb45db2,,,,,,
Ui3Of5Nz,CM 431 - Maintenance painting of steelwork,https://www.standardsforhighways.co.uk/search/1c6a08d2-94af-4a35-9fa1-bdabdb90ff12,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for, and gives advice on, the development of
maintenance painting schemes and specifications for steelwork in highway structures. The
document also provides details of bespoke maintenance painting specifications that have been
developed to address specific maintenance painting situations.",17/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Steelwork
Painting
Specification
Weathering steel",Active,,,,,,https://www.standardsforhighways.co.uk/search/1c6a08d2-94af-4a35-9fa1-bdabdb90ff12,,,,,,
Fy7Uw2Mi,CM 432 - Maintenance of buried concrete box structures,https://www.standardsforhighways.co.uk/search/4eb09170-3115-4bd0-8d11-ffda4bae3033,nationalhighways,National Highways ,eng,HTML,This document details the maintenance requirements for buried concrete box structures.,18/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Buried concrete box structures
Maitenance
Defects",Active,,,,,,https://www.standardsforhighways.co.uk/search/4eb09170-3115-4bd0-8d11-ffda4bae3033,,,,,,
Ku9Dx0Yw,CS 125 - Inspection of traffic signs,https://www.standardsforhighways.co.uk/search/3e1d3100-4e91-4389-bfab-b0648f9539c1,nationalhighways,National Highways ,eng,HTML,This document sets out the requirements for the inspection of permanent traffic signs.,19/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Traffic signs
Inspection
Defects
Inventory",Active,,,,,,https://www.standardsforhighways.co.uk/search/3e1d3100-4e91-4389-bfab-b0648f9539c1,,,,,,
Bc7Vz0Ga,CS 126 - Inspection and assessment of road markings and road studs,https://www.standardsforhighways.co.uk/search/d05b10c6-31b8-4110-a805-d6bd9e4d41d4,nationalhighways,National Highways ,eng,HTML,"This document provides general information to support the inspection and assessment of the
road marking and road stud asset. It specifically clarifies the risk based approach when
considering renewal of these assets.",20/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Inspection
Road markings
Road studs
Defects",Active,,,,,,https://www.standardsforhighways.co.uk/search/d05b10c6-31b8-4110-a805-d6bd9e4d41d4,,,,,,
Lc4Xw3Ns,CS 228 HE Crash Model - Highways England Crash Model,https://www.standardsforhighways.co.uk/search/c6d72999-cef1-495e-a636-d74800aba167,nationalhighways,National Highways ,eng,HTML,HE Crash Model - Highways England Crash Model,21/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,,Active,,,,,,https://www.standardsforhighways.co.uk/search/c6d72999-cef1-495e-a636-d74800aba167,,,,,,
Vy8Au6Pu,CS 228 - Skidding resistance,https://www.standardsforhighways.co.uk/search/50d43081-9726-41e8-9835-9cd55760ad9e,nationalhighways,National Highways ,eng,HTML,"This document describes the requirements for the provision and management of appropriate
levels of skid resistance on UK motorway and all-purpose trunk roads.",22/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Skidding
Skid resistance
Slippery road warning",Active,,,,,,https://www.standardsforhighways.co.uk/search/50d43081-9726-41e8-9835-9cd55760ad9e,,,,,,
Me6Ow8Ox,CS 229 - Data for pavement assessment,https://www.standardsforhighways.co.uk/search/2e9e1b1c-528a-4b7d-bea8-d1c49a3caded,nationalhighways,National Highways ,eng,HTML,"This document describes the technical requirements for undertaking detailed scheme-level
pavement investigations on the UK motorway and all-purpose trunk roads.",23/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Pavement assessment
Falling weight deflectometer
Ground-penetrating radar
Invasive testing",Active,,,,,,https://www.standardsforhighways.co.uk/search/2e9e1b1c-528a-4b7d-bea8-d1c49a3caded,,,,,,
Hh8Qe9Yn,CS 230 - Pavement maintenance assessment procedure,https://www.standardsforhighways.co.uk/search/html/5c21c19f-4292-4764-86f6-bbb51df313e0?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document sets out the requirements for reviewing routine/network level data in order to establish whether there is a pavement maintenance need that requires further investigation.,24/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Pavement maintenance
Surveys
Network level surveys",Active,,,,,,https://www.standardsforhighways.co.uk/search/5c21c19f-4292-4764-86f6-bbb51df313e0,,,,,,
Wj3Qf4Ya,CS 432 - Inspection of buried concrete box structures,https://www.standardsforhighways.co.uk/search/3a77040a-a018-4485-aea1-9f4fd379b7a9,nationalhighways,National Highways ,eng,HTML,This document details the inspection requirements for buried concrete box structures,25/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Buried concrete box structures
Inspection",Active,,,,,,https://www.standardsforhighways.co.uk/search/3a77040a-a018-4485-aea1-9f4fd379b7a9,,,,,,
Kd9Cg5To,CS 450 - Inspection of highway structures,https://www.standardsforhighways.co.uk/search/html/c5c2c3e5-f7f3-4c94-8254-184e41ccd1a0?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document gives the Overseeing Organisation's requirements for inspection of its highway structures.,26/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Highway structures
Inspection
Maintenance
Health and safety",Active,,,,,,https://www.standardsforhighways.co.uk/search/c5c2c3e5-f7f3-4c94-8254-184e41ccd1a0,,,,,,
Pn5Yp7Wv,CS 451 - Structural review and assessment of highway structures,https://www.standardsforhighways.co.uk/search/81489ab4-7e79-4139-9822-104fa460cd84,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for structural review and assessment of highway
structures.",27/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Structural review
Highway structures",Active,,,,,,https://www.standardsforhighways.co.uk/search/81489ab4-7e79-4139-9822-104fa460cd84,,,,,,
So4Ub6Vy,CS 452 - Inspection and records for road tunnel systems,https://www.standardsforhighways.co.uk/search/5b571cfa-63a8-4c58-bdc2-c2c5f0390834,nationalhighways,National Highways ,eng,HTML,This document describes the procedures for inspection and recording arrangements for road tunnels on the motorway and all-purpose trunk road network.,28/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Inspection
Road tunnel
Record keeping",Active,,,,,,https://www.standardsforhighways.co.uk/search/5b571cfa-63a8-4c58-bdc2-c2c5f0390834,,,,,,
Rt7Uj9Ng,CS 453 - The assessment of highway bridge supports,https://www.standardsforhighways.co.uk/search/dc121d82-3708-4b40-89c9-9cc0d520fa7b,nationalhighways,National Highways ,eng,HTML,"This document outlines the requirements for the assessment and strengthening of highway
bridge supports.",29/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Assessment
Strengthening
Highway bridge supports
Collision loading",Active,,,,,,https://www.standardsforhighways.co.uk/search/dc121d82-3708-4b40-89c9-9cc0d520fa7b,,,,,,
Qt7Sd7Kh,CS 454 - Assessment of highway bridges and structures,https://www.standardsforhighways.co.uk/search/html/96569268-6c26-4263-a1f7-bc09a9e3977f?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"The use of this document enables the structural safety and serviceability of highway bridges and structures to be assessed, providing key information that is required to manage risks and maintain a safe and operational network.",30/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Highway bridges
Highway structures
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/96569268-6c26-4263-a1f7-bc09a9e3977f,,,,,,
Lu7Ad2To,CS 455 - The assessment of concrete highway bridges and structures,https://www.standardsforhighways.co.uk/search/html/3e813e52-da54-4c84-830c-25c0f6960a5f?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"The use of this document enables the concrete highway bridges and structures to be assessed, providing key information that is required to manage risks and maintain a safe and operational network.",31/01/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Concrete
Highways bridges
Highway structures
Reinorced concrete beams
Prestressed concrete",Active,,,,,,https://www.standardsforhighways.co.uk/search/3e813e52-da54-4c84-830c-25c0f6960a5f,,,,,,
Vk6Ux5Ks,CS 456 - The assessment of steel highway bridges and structures,https://www.standardsforhighways.co.uk/search/5f9b8d2c-e993-4f26-aa1b-3e7426347251,nationalhighways,National Highways ,eng,HTML,"This document gives requirements for the assessment of existing steel structures and structural
element on motorways and other trunk roads.",01/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Steel highways bridges
Steel highway structures
Static structures
Fatigue",Active,,,,,,https://www.standardsforhighways.co.uk/search/5f9b8d2c-e993-4f26-aa1b-3e7426347251,,,,,,
Yw5Ga8Cn,CS 457 - The assessment of composite highway bridges and structures,https://www.standardsforhighways.co.uk/search/bc023d12-6699-4788-a6b0-cab72506ad3f,nationalhighways,National Highways ,eng,HTML,"This document contains requirements for the assessment of existing steel/concrete composite
structures and structural elements.",02/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Composite highway bridges
Composite highway structures
Assessment
Structural analysis
Box girders
Columns",Active,,,,,,https://www.standardsforhighways.co.uk/search/bc023d12-6699-4788-a6b0-cab72506ad3f,,,,,,
Vg6Vi3Op,CS 458 - The assessment of highway bridges and structures for the effects of special type general order (STGO) and special order (SO) vehicles,https://www.standardsforhighways.co.uk/search/a957dd8d-d61f-47fa-8902-defc2a335760,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the assessment of highway bridges and structures
to determine the effects of special type general order (STGO) and special order (SO) vehicles.",03/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Highway bridges
Vehicle impacts
Special order vehicles",Active,,,,,,https://www.standardsforhighways.co.uk/search/a957dd8d-d61f-47fa-8902-defc2a335760,,,,,,
Uc9Ot0Jw,"CS 459 - The assessment of bridge substructures, retaining structures and buried structures",https://www.standardsforhighways.co.uk/search/70f7c960-f24a-4831-967b-ad1acb028c1a,nationalhighways,National Highways ,eng,HTML,"The use of this document enables the safety and serviceability of bridge substructures, retaining
structures and buried structures to be assessed, providing key information that is required to
manage risks and maintain a safe and operational network.",04/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Bridges
Substructures
Retaining structures
Buried structures
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/70f7c960-f24a-4831-967b-ad1acb028c1a,,,,,,
Gn7Uw9Qe,CS 460 - Management of corrugated steel buried structures,https://www.standardsforhighways.co.uk/search/html/10307389-0824-4231-857e-0fe6468b47e0?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document details the management requirements for corrugated steel buried structures.,05/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Corrugated steel
Buried structures
Inspection
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/10307389-0824-4231-857e-0fe6468b47e0,,,,,,
Al5Zw6Pa,CS 461 - Assessment and upgrading of in-service parapets,https://www.standardsforhighways.co.uk/search/5e5350e7-3f54-4a4e-8f78-303ebdef9e4a,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for the assessment and upgrading of existing
vehicle parapets on highway structures. It gives advice on the assessment of parapet and safety
barrier supporting members on bridges and retaining walls.",06/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Parapets
Risk assessment
Parapet remnant containment resistance
Obselete parapets",Active,,,,,,https://www.standardsforhighways.co.uk/search/5e5350e7-3f54-4a4e-8f78-303ebdef9e4a,,,,,,
Fb6Fe5Ar,CS 462 - Repair and management of deteriorated concrete highway structures,https://www.standardsforhighways.co.uk/search/cbd1b3e5-af18-44a2-abfc-91c457e01b7e,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for repair or management in service of
deteriorated concrete highway structures.",07/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Concrete highway structures
Deterioration
Assessment
Protect and repair strategy",Active,,,,,,https://www.standardsforhighways.co.uk/search/cbd1b3e5-af18-44a2-abfc-91c457e01b7e,,,,,,
Hc4Tf0Ac,CS 463 - Load testing for bridge assessment,https://www.standardsforhighways.co.uk/search/3aca0a30-93a3-4ffa-8164-07735bb29a5c,nationalhighways,National Highways ,eng,HTML,"This document describes the requirements for load tests to be used to assist in the strength
assessment of bridges.",08/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Bridges
Load testing",Active,,,,,,https://www.standardsforhighways.co.uk/search/3aca0a30-93a3-4ffa-8164-07735bb29a5c,,,,,,
Vf0Ix2Rw,CS 464 - Non-destructive testing of highways structures,https://www.standardsforhighways.co.uk/search/f9ea394a-0d4b-4e64-8bf9-73b330403832,nationalhighways,National Highways ,eng,HTML,"This document sets out requirements regarding the non-destructive testing of highways
structures.",09/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Highway structures
Non-destructive testing
Record taking
",Active,,,,,,https://www.standardsforhighways.co.uk/search/f9ea394a-0d4b-4e64-8bf9-73b330403832,,,,,,
Yd9Hk4Ek,CS 465 - Management of post-tensioned concrete bridges,https://www.standardsforhighways.co.uk/search/3eab3df6-b87b-412d-ac0b-87a1ea1c325c,nationalhighways,National Highways ,eng,HTML,"This document provides a process of risk review, risk assessment and risk management for
post-tensioned concrete bridges to provide assurance on the safety of the stock of those bridges.",10/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Post-tensioned concrete bridges
Repair
Strengthening
Monitoring",Active,,,,,,https://www.standardsforhighways.co.uk/search/3eab3df6-b87b-412d-ac0b-87a1ea1c325c,,,,,,
Pe4Mp3Yf,CS 466 - Risk management and structural assessment of concrete half-joint deck structures,https://www.standardsforhighways.co.uk/search/fb88f0a1-6723-47f7-967f-5abc4cd38ec6,nationalhighways,National Highways ,eng,HTML,"The use of this document enables the safety and serviceability of half-joints to be managed and
assessed, providing key information that is required to manage risks and maintain a safe and
operational network.",11/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Concrete half-joint deck structures
Risk management
Structural assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/fb88f0a1-6723-47f7-967f-5abc4cd38ec6,,,,,,
Db6Ar6Xv,CS 467 - Risk management and structural assessment of concrete deck hinge structures,https://www.standardsforhighways.co.uk/search/a5411e11-d9af-4c13-8566-9f96d6716e69,nationalhighways,National Highways ,eng,HTML,"The use of this document enables the safety and serviceability of concrete hinge deck structures
to be assessed and managed, allowing to manage risks and maintain a safe and operational
network.",12/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Concrete  deck hinge structures
Risk management
Structural assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/a5411e11-d9af-4c13-8566-9f96d6716e69,,,,,,
El7Uq6Vb,CS 468 - Assessment of Freyssinet concrete hinges in highway structures,https://www.standardsforhighways.co.uk/search/9305895c-ccce-4e9e-889b-b1d9dcffd25b,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for the assessment of Freyssinet concrete hinges used
in highway structures. It also provides advice on the inspection and management of Freyssinet
concrete hinges.",13/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Freyssinet concrete hinges
Highway structures
Assessment
Inspection",Active,,,,,,https://www.standardsforhighways.co.uk/search/9305895c-ccce-4e9e-889b-b1d9dcffd25b,,,,,,
Jv3Zl3Nx,CS 469 - Management of scour and other hydraulic actions at highway structures.,https://www.standardsforhighways.co.uk/search/html/056a01ec-4028-4a07-9a21-7168c952cc99?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and advice for the management of scour and other hydraulic actions at structures. This document provides processes, to determine the level of risk associated with structural damage, caused by scour and other hydraulic actions on structures in severe weather events. This document includes allowances for climate change. This document provides advice on mitigating actions which could potentially reduce risks, caused by scour and other hydraulic actions on structures.",14/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Scour susceptible structures
Inspection
Assessment
Hydraulic action
Risk management",Active,,,,,,https://www.standardsforhighways.co.uk/search/056a01ec-4028-4a07-9a21-7168c952cc99,,,,,,
Of7Kj4Jo,CS 470 - Management of sub-standard highway structures,https://www.standardsforhighways.co.uk/search/8d9db6a3-55e2-4947-855a-98ae3db77fc5,nationalhighways,National Highways ,eng,HTML,"This document sets out the procedures for managing highway structures that have been found to
be sub-standard",15/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Sub-standard
Highway structure
Immediate risk
Interim measures
Record keeping",Active,,,,,,https://www.standardsforhighways.co.uk/search/8d9db6a3-55e2-4947-855a-98ae3db77fc5,,,,,,
Vh4Ec1Ky,CS 551 - Drainage surveys,https://www.standardsforhighways.co.uk/search/553070d2-facb-428c-a1fa-40c7fd52fd70,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for highway drainage surveys.,16/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Drainage
Validation
Priority assets
Filter drain
Pipework
Chambers
Soil sampling",Active,,,,,,https://www.standardsforhighways.co.uk/search/553070d2-facb-428c-a1fa-40c7fd52fd70,,,,,,
Xo5Bd0On,CS 641 - Managing the maintenance of highway geotechnical assets,https://www.standardsforhighways.co.uk/search/1281942c-6da0-40e7-83db-3c37c44211cf,nationalhighways,National Highways ,eng,HTML,"This document defines the roles of organisations and people in the management of geotechnical
assets, the planning and risk management of activities undertaken on geotechnical assets and
defines the associated information requirements.",17/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Geotechnical asset
Management plan
Inspections
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/1281942c-6da0-40e7-83db-3c37c44211cf,,,,,,
Re1Tj0Bx,CZ 125 - Disposal of traffic signs,https://www.standardsforhighways.co.uk/search/3923e4f2-82b0-43e9-81ac-b8f2aec6b84d,nationalhighways,National Highways ,eng,HTML,This document sets out the requirements for the disposal of permanent traffic signs.,18/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Traffic Signs
Removal
Replacement",Active,,,,,,https://www.standardsforhighways.co.uk/search/3923e4f2-82b0-43e9-81ac-b8f2aec6b84d,,,,,,
Vi4My8Pc,GAMP - General Asbestos Management Plan,https://www.standardsforhighways.co.uk/search/8af41f54-f5b1-4a38-879d-35c4c03590fa,nationalhighways,National Highways ,eng,HTML,"HA Strategic Network General
Asbestos Management Plan
(GAMP)",19/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Asbestos
Management",Active,,,,,,https://www.standardsforhighways.co.uk/search/8af41f54-f5b1-4a38-879d-35c4c03590fa,,,,,,
Bj6Yd5Gg,GD 300 - Requirements for new and upgraded all-purpose trunk roads (expressways),https://www.standardsforhighways.co.uk/search/1223f3d1-5dd8-4afd-a2e8-0367f70b8652,nationalhighways,National Highways ,eng,HTML,"This document provides the design requirements and advice for new and upgraded all-purpose
trunk roads (expressways).
",20/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
All-purpose trunk roads",Active,,,,,,https://www.standardsforhighways.co.uk/search/1223f3d1-5dd8-4afd-a2e8-0367f70b8652,,,,,,
Se6Xk9Ed,GD 301 - Smart motorways,https://www.standardsforhighways.co.uk/search/d908f9c2-cd47-4e96-b015-97b51e24c588,nationalhighways,National Highways ,eng,HTML,This document sets out the design requirements and advice for smart motorways.,21/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Smart motorways",Active,,,,,,https://www.standardsforhighways.co.uk/search/d908f9c2-cd47-4e96-b015-97b51e24c588,,,,,,
Va0Dw2Cj,GD 304 - Designing health and safety into maintenance,https://www.standardsforhighways.co.uk/search/92f8fac5-b0e7-4039-8e7d-a5ff007a1332,nationalhighways,National Highways ,eng,HTML,This document contains requirements related to designing health and safety into maintenance.,22/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Health and safety
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/92f8fac5-b0e7-4039-8e7d-a5ff007a1332,,,,,,
Oj6Hb9Sh,GD 368 - Infrastructure requirements for emergency access and egress from motorway and all-purpose trunk roads,https://www.standardsforhighways.co.uk/search/8ef4825b-f9ec-4c0a-b60b-0ffb40613e83,nationalhighways,National Highways ,eng,HTML,"This document contains the infrastructure requirements for emergency access and egress from
motorway and all-purpose trunk roads.",23/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Emergency access
Motorways
All-purpose trunk roads",Active,,,,,,https://www.standardsforhighways.co.uk/search/8ef4825b-f9ec-4c0a-b60b-0ffb40613e83,,,,,,
Fc7Ly5Iu,GD 904 - The use of highest safe speed limits including advice on using 60mph at/through road works,https://www.standardsforhighways.co.uk/search/d2a7e3f6-069c-4dc8-9277-10ab532ab429,nationalhighways,National Highways ,eng,HTML,"This standard contains the requirements for the use of highest safe speed limits and includes
advice on the use of 60mph temporary speed limits at/through road works.",24/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Speed limits
Road works",Active,,,,,,https://www.standardsforhighways.co.uk/search/d2a7e3f6-069c-4dc8-9277-10ab532ab429,,,,,,
Xk9Rv2Wn,GG 102 - Quality management systems for highway works,https://www.standardsforhighways.co.uk/search/745cf41e-48c1-4096-972a-5a65cc48981c,nationalhighways,National Highways ,eng,HTML,"This document gives the requirements in respect of quality management systems for
organisations carrying out any or all activities for permanent and temporary works on behalf of
the Overseeing Organisation. It provides additional requirements to ISO 9001:2015 for the
development and use of project-specific quality management plans.",25/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Quality management
Leadership
Planning
Operation
Support
Performance evaluation
Improvement",Active,,,,,,https://www.standardsforhighways.co.uk/search/745cf41e-48c1-4096-972a-5a65cc48981c,,,,,,
Sc3We4Ux,GG 103 - Introduction and general requirements for sustainable development and design,https://www.standardsforhighways.co.uk/search/89d10ef2-7833-44df-9140-df85cd6382b9,nationalhighways,National Highways ,eng,HTML,This document introduces the general requirements for sustainable development and design.,26/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Sustainable development
Legal
Environmental
Economic
Social
Cultural",Active,,,,,,https://www.standardsforhighways.co.uk/search/89d10ef2-7833-44df-9140-df85cd6382b9,,,,,,
Ev7Sf3Wi,GG 104 - Requirements for safety risk assessment,https://www.standardsforhighways.co.uk/search/0338b395-7959-4e5b-9537-5d2bdd75f3b9,nationalhighways,National Highways ,eng,HTML,"This document sets out the approach for safety risk assessment to be applied when undertaking
any activity that does or can have an impact on safety on Highways England's motorway and
all-purpose trunk roads, either directly or indirectly. It provides a framework for identifying hazards,
assessing, evaluating and managing safety risks and assuring safety risk governance. This
document only applies to Highways England.",27/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Safety risk assessment
Hazards",Active,,,,,,https://www.standardsforhighways.co.uk/search/0338b395-7959-4e5b-9537-5d2bdd75f3b9,,,,,,
Vq7Cc7Ui,GG 105 - Asbestos management,https://www.standardsforhighways.co.uk/search/9f7803ca-26aa-49bd-98f8-c514ab051040,nationalhighways,National Highways ,eng,HTML,"This document sets out management processes and legal requirements for asbestos
management in trunk road assets.",28/02/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Asbestos
Surveys",Active,,,,,,https://www.standardsforhighways.co.uk/search/9f7803ca-26aa-49bd-98f8-c514ab051040,,,,,,
Nb8Lv7Ft,GG 115 - Requirements for works on the hard shoulder and road side verges on high speed dual carriageways,https://www.standardsforhighways.co.uk/search/f6a79f63-f077-4b67-ae0b-390ad229a9e7,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for works on the hard shoulder and road side verges
on high speed dual carriageways",01/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road works
Hard shoulder
Dual carriageways",Active,,,,,,https://www.standardsforhighways.co.uk/search/f6a79f63-f077-4b67-ae0b-390ad229a9e7,,,,,,
Ap0Td2Mt,"GG 116 - Requirements and guidance on temporary traffic management short term lane closures for relaxation works, types 0, 1 and 2",https://www.standardsforhighways.co.uk/search/2489f719-1c2f-4c1f-af31-e3418d5fe1a3,nationalhighways,National Highways ,eng,HTML,"This document provides requirements and guidance on temporary traffic management short term
lane closures for relaxation works, types 0, 1 and 2",02/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road works
Traffic management
Lane closures",Active,,,,,,https://www.standardsforhighways.co.uk/search/2489f719-1c2f-4c1f-af31-e3418d5fe1a3,,,,,,
Zi1Mk6Is,GG 117 - The design and implementation of temporary traffic management and road works,https://www.standardsforhighways.co.uk/search/html/4ee0b2ef-5f44-4299-8920-4eac79b1603c?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This standard gives the requirements for the design and implementation of temporary traffic management,03/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road works
Traffic management
Temporary
Road closures",Active,,,,,,https://www.standardsforhighways.co.uk/search/4ee0b2ef-5f44-4299-8920-4eac79b1603c,,,,,,
Sc9Ay1Jy,GG 119 - Road safety audit,https://www.standardsforhighways.co.uk/search/710d4c33-0032-4dfb-8303-17aff1ce804b,nationalhighways,National Highways ,eng,HTML,"This document provides the requirements for road safety audit for highway schemes on the trunk
road and motorway network.",04/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Road safety audit
Process requirements
Certificate of competency",Active,,,,,,https://www.standardsforhighways.co.uk/search/710d4c33-0032-4dfb-8303-17aff1ce804b,,,,,,
Bl2Lx4Rh,"GG 128 - Requirements for reporting incidents, events and undesirable circumstances: health, safety, wellbeing, structural and environmental",https://www.standardsforhighways.co.uk/search/e86b7699-ed01-4806-a0fc-9fe11c8e73ee,nationalhighways,National Highways ,eng,HTML,"This document contains requirements for the reporting of incidents and events and undesirable
circumstances: health, safety, wellbeing, structural and environmental.",05/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highways design
Design requirements
Peporting
Incidents
Health and safety",Active,,,,,,https://www.standardsforhighways.co.uk/search/e86b7699-ed01-4806-a0fc-9fe11c8e73ee,,,,,,
Ij3Ma4Zk,"GG 142 - Walking, cycling and horse-riding assessment and review",https://www.standardsforhighways.co.uk/search/5f33456d-32f9-4822-abf6-e12510f5c8dc,nationalhighways,National Highways ,eng,HTML,"This document sets out the walking, cycling and horse-riding assessment and review (WCHAR)
process for highway schemes on motorways and all-purpose trunk roads.",06/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Highway assessment
Walking
Cycling
Horse-riding",Active,,,,,,https://www.standardsforhighways.co.uk/search/5f33456d-32f9-4822-abf6-e12510f5c8dc,,,,,,
Fd9Vm5Sv,GG 182 - Major schemes: Enabling handover into operation and maintenance,https://www.standardsforhighways.co.uk/search/8027744b-971d-4ca7-ba6d-cf8fd03201af,nationalhighways,National Highways ,eng,HTML,"This document contains requirements related to major schemes: enabling handover into
operation and maintenance.",07/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Major schemes
Handover
Operation
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/8027744b-971d-4ca7-ba6d-cf8fd03201af,,,,,,
Cd3Qb3Gw,GG 184 - Specification for the use of Computer Aided Design,https://www.standardsforhighways.co.uk/search/f184cf11-a54c-4f82-9a79-e5ff4332daf0,nationalhighways,National Highways ,eng,HTML,"This document contains specifications for the use of Computer Aided Design (CAD). It defines
methods for managing the production, distribution and quality of construction information using
CAD systems, through a disciplined process for collaboration and a specified naming convention.",08/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Computer Aided Design
CAD
Construction quality",Active,,,,,,https://www.standardsforhighways.co.uk/search/f184cf11-a54c-4f82-9a79-e5ff4332daf0,,,,,,
Ee3Rr6Ss,GG 901 - Customer service standard for the quality and timeliness of responses to customer contact,https://www.standardsforhighways.co.uk/search/html/dc2e2ad2-72da-4e53-ab97-5f52c174f59f?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains requirements for the quality and timeliness of responses to customer contact.,09/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Customer service
Timeliness
Response quality",Active,,,,,,https://www.standardsforhighways.co.uk/search/dc2e2ad2-72da-4e53-ab97-5f52c174f59f,,,,,,
Yl8Rm6Lz,GG 902 - Customer service standard for accurate advance notification of planned closures,https://www.standardsforhighways.co.uk/search/html/33e542bd-e750-467c-a39e-7531304470e6?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"This document contains the customer service standard requirements for accurate advance notification of planned closures.
",10/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Customer service
Advanced notice
Planned closure",Active,,,,,,https://www.standardsforhighways.co.uk/search/33e542bd-e750-467c-a39e-7531304470e6,,,,,,
Kf1Bw0Ut,GG 903 - Customer service standard for diversion routes for unplanned events,https://www.standardsforhighways.co.uk/search/125f41ee-969c-4b6d-8951-c353c4bfd432,nationalhighways,National Highways ,eng,HTML,"This document contains the customer service standard requirements for diversion routes for
unplanned events.",11/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Customer service
Diversion
Routes
Unplanned events",Active,,,,,,https://www.standardsforhighways.co.uk/search/125f41ee-969c-4b6d-8951-c353c4bfd432,,,,,,
Bx9Af9Wg,GG 906 - Customer service standard for scheme billboards,https://www.standardsforhighways.co.uk/search/html/77b85366-7cd7-4a3e-9f56-ba3fe3f55013?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains requirements for the provision of scheme billboards providing roadwork information to customers.,12/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Customer service
Scheme billboards
Roadwork information",Active,,,,,,https://www.standardsforhighways.co.uk/search/77b85366-7cd7-4a3e-9f56-ba3fe3f55013,,,,,,
Rn3Pp4Gg,GG 907 - Customer service standard for diversion routes for planned works and activities,https://www.standardsforhighways.co.uk/search/html/e7919b54-d6a4-49df-8b5a-ce2c0228eab9?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the customer service standard requirements for diversion routes for planned works and activities..,13/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Customer service
Diversion
Routes
Planned works
Planned activities",Active,,,,,,https://www.standardsforhighways.co.uk/search/e7919b54-d6a4-49df-8b5a-ce2c0228eab9,,,,,,
Zh7Vb4Fy,GG 951 - General requirements for geomatical surveys,https://www.standardsforhighways.co.uk/search/html/6433dd92-5d49-42c0-b79e-2bea56676ce5?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the overarching requirements for the undertaking of geomatical surveys and provision of geomatic survey data.,14/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Geomatical surveys
Untertaking surveys",Active,,,,,,https://www.standardsforhighways.co.uk/search/6433dd92-5d49-42c0-b79e-2bea56676ce5,,,,,,
Xo9Kr2Mz,GG 953 - Local grid layout for England digital map,https://www.standardsforhighways.co.uk/search/0781acd0-8238-464a-ba8a-a4e249dcc56c,nationalhighways,National Highways ,eng,HTML,Local grid layout for England digital map,15/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"England map
Digital map
Local grid
Grid layout",Active,,,,,,https://www.standardsforhighways.co.uk/search/0781acd0-8238-464a-ba8a-a4e249dcc56c,,,,,,
Ma9Px0On,GG 954 - Drones operations,https://www.standardsforhighways.co.uk/search/html/ce7e41ba-3dc1-41de-bf25-4f8da7b2bb06?standard=DMRB,nationalhighways,National Highways ,eng,HTML,"This document details requirements that govern the use of Unmanned Aerial Systems, commonly referred to as 'drones', for or on behalf of the Overseeing Organisation.",16/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Drone operation
Unmanned aerial systems
Usage limits",Active,,,,,,https://www.standardsforhighways.co.uk/search/ce7e41ba-3dc1-41de-bf25-4f8da7b2bb06,,,,,,
Kp2Rk7Pr,GM 701 - Asset delivery asset maintenance requirements,https://www.standardsforhighways.co.uk/search/e0a134c8-f5e2-4f30-9cda-9e43d047f46e,nationalhighways,National Highways ,eng,HTML,"This document contains asset delivery asset maintenance requirements for motorways and
all-purpose trunk roads.",17/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Asset delivery
Maintenance requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/e0a134c8-f5e2-4f30-9cda-9e43d047f46e,,,,,,
Zd6Xp1Fw,GM 702 - Operational requirements for network occupancy,https://www.standardsforhighways.co.uk/search/html/1448db77-e9dd-497b-b089-56a6704ff7e5?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the operational requirements for network occupancy.,18/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Network occupancy
Operational requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/1448db77-e9dd-497b-b089-56a6704ff7e5,,,,,,
Fm1Oa3Kv,GM 703 - Operational requirements for incident management,https://www.standardsforhighways.co.uk/search/fce4e513-080b-4d96-99ca-b653612c77ee,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the management and response activities for all
incidents on motorways and all-purpose trunk roads.",19/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Incident management
Response activities",Active,,,,,,https://www.standardsforhighways.co.uk/search/fce4e513-080b-4d96-99ca-b653612c77ee,,,,,,
Wz6Pc7Qg,GM 704 - Operational requirements for severe weather,https://www.standardsforhighways.co.uk/search/02036725-1e02-487f-8eb3-244741f44aae,nationalhighways,National Highways ,eng,HTML,This document sets out requirements in relation to the delivery of the severe weather service.,20/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Severe weather
Service provision",Active,,,,,,https://www.standardsforhighways.co.uk/search/02036725-1e02-487f-8eb3-244741f44aae,,,,,,
Tp5Na2Mn,GS 801 - Asset delivery asset inspection requirements,https://www.standardsforhighways.co.uk/search/6b558352-5c85-4725-b5f2-f796f53d63a8,nationalhighways,National Highways ,eng,HTML,"This document contains inspection and assessment requirements for motorways and all-purpose
trunk roads.",21/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Asset delivery
Maintenance requirements
Inspection requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/6b558352-5c85-4725-b5f2-f796f53d63a8,,,,,,
Ui3Tv8Tg,GS 952 - Requirements for topographical surveys,https://www.standardsforhighways.co.uk/search/html/ddce77ef-55ee-423c-a9c6-a18d2e18de3a?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for undertaking topographical surveys and provision topographical survey data supplementary to GG 951.,22/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Topographical survey
Supplementary data",Active,,,,,,https://www.standardsforhighways.co.uk/search/ddce77ef-55ee-423c-a9c6-a18d2e18de3a,,,,,,
Np2Fl7Rv,LA 101 - Introduction to environmental assessment,https://www.standardsforhighways.co.uk/search/54b0eb69-fd65-4fa5-a86b-7313f70b3649,nationalhighways,National Highways ,eng,HTML,"This document sets out the over-arching requirements and principles that form an introduction to
the environmental assessment of motorway and all-purpose trunk roads.",23/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Environmental assessment,Active,,,,,,https://www.standardsforhighways.co.uk/search/54b0eb69-fd65-4fa5-a86b-7313f70b3649,,,,,,
Kb2Wh2Us,LA 102 - Screening projects for Environmental Impact Assessment,https://www.standardsforhighways.co.uk/search/dc73affe-4f24-4077-8637-e79e4fb7b198,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements on screening projects for Environmental Impact
Assessment in line with Directive 2011/92/EU as amended by 2014/52/EU.",24/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Screening projects
Environmental Impact Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/dc73affe-4f24-4077-8637-e79e4fb7b198,,,,,,
Ag3Nv1Ft,LA 103 - Scoping projects for environmental assessment,https://www.standardsforhighways.co.uk/search/fb43a062-65ad-48d3-8c06-374cfd3b8c23,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for scoping motorway and all-purpose trunk road
projects for environmental assessment.",25/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Scoping projects
Environmental assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/fb43a062-65ad-48d3-8c06-374cfd3b8c23,,,,,,
Wg6An7Uh,LA 104 - Environmental assessment and monitoring,https://www.standardsforhighways.co.uk/search/0f6e0b6a-d08e-4673-8691-cab564d4a60a,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for environmental assessment of projects, including
reporting and monitoring of significant adverse environmental effects.
",26/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Environmental assessment
Monitoring
Adverse environmental impacts",Active,,,,,,https://www.standardsforhighways.co.uk/search/0f6e0b6a-d08e-4673-8691-cab564d4a60a,,,,,,
Pb6Iy5Cw,LA 105 - Air quality,https://www.standardsforhighways.co.uk/search/html/af7f4cda-08f7-4f16-a89f-e30da703f3f4?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document sets out the requirements for assessing and reporting the effects of highway projects on air quality.,27/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Air quality
Asessing
Reporting
Effects",Active,,,,,,https://www.standardsforhighways.co.uk/search/af7f4cda-08f7-4f16-a89f-e30da703f3f4,,,,,,
Kf1Cx9Jk,LA 106 - Cultural heritage assessment,https://www.standardsforhighways.co.uk/search/8c51c51b-579b-405b-b583-9b584e996c80,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects on cultural
heritage as part of the environmental assessment process of construction, operation and
maintenance projects.",28/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Cultural heritage assessment
Environmental Assessment
Operation
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/8c51c51b-579b-405b-b583-9b584e996c80,,,,,,
Nz6Gu7Sc,LA 107 - Landscape and visual effects,https://www.standardsforhighways.co.uk/search/bc8a371f-2443-4761-af5d-f37d632c5734,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for assessing and reporting the landscape and visual
effects of highway projects.",29/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Landscape
Visual effects
Assessing
Reporting",Active,,,,,,https://www.standardsforhighways.co.uk/search/bc8a371f-2443-4761-af5d-f37d632c5734,,,,,,
Wg9Zq3Rc,LA 108 - Biodiversity,https://www.standardsforhighways.co.uk/search/af0517ba-14d2-4a52-aa6d-1b21ba05b465,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects of highway
projects on biodiversity.",30/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Biodiversity
Assessing
Reporting",Active,,,,,,https://www.standardsforhighways.co.uk/search/af0517ba-14d2-4a52-aa6d-1b21ba05b465,,,,,,
Bi5Mm0Pk,LA 109 - Geology and soils,https://www.standardsforhighways.co.uk/search/adca4c7d-4037-4907-b633-76eaed30b9c0,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects of highway
projects on geology and soils.",31/03/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Geology
Soils
Assessing
Reporting",Active,,,,,,https://www.standardsforhighways.co.uk/search/adca4c7d-4037-4907-b633-76eaed30b9c0,,,,,,
Kc9Zb0Im,LA 110 - Material assets and waste,https://www.standardsforhighways.co.uk/search/6a19a7d4-2596-490d-b17b-4c9e570339e9,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects on material
assets and waste from the delivery of motorway and all-purpose trunk road projects.",01/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Material assets
Waste
Assessing
Reporting",Active,,,,,,https://www.standardsforhighways.co.uk/search/6a19a7d4-2596-490d-b17b-4c9e570339e9,,,,,,
Po9Fk5Ru,LA 111 - Noise and vibration,https://www.standardsforhighways.co.uk/search/cc8cfcf7-c235-4052-8d32-d5398796b364,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects of highways
noise and vibration from construction, operation and maintenance projects. The document has
been updated to correct time periods in Tables 3.12 and 3.49.1, update the references for speed
pivoting requirements in Appendix A2, and to clarify other requirements following feedback
received.",02/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Noise
Vibration
Construction
Operation
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/cc8cfcf7-c235-4052-8d32-d5398796b364,,,,,,
Jq4Vd8Be,LA 112 - Population and human health,https://www.standardsforhighways.co.uk/search/1e13d6ac-755e-4d60-9735-f976bf64580a,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the environmental effects
on population and health from construction, operation and maintenance of highways projects.",03/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Population
Human health
Assessing
Reporting
Construction
Operation
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/1e13d6ac-755e-4d60-9735-f976bf64580a,,,,,,
Gu4Es1Ib,LA 113 - Road drainage and the water environment,https://www.standardsforhighways.co.uk/search/d6388f5f-2694-4986-ac46-b17b62c21727,nationalhighways,National Highways ,eng,HTML,"This document describes the requirements for assessment and management of the impacts that
road projects can have on the water environment.",04/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road drainage
Water environment
Assessment
Management",Active,,,,,,https://www.standardsforhighways.co.uk/search/d6388f5f-2694-4986-ac46-b17b62c21727,,,,,,
Va0Kl4Qr,LA 114 - Climate,https://www.standardsforhighways.co.uk/search/d1ec82f3-834b-4d5f-89c6-d7d7d299dce0,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessing and reporting the effects of climate on
highways (climate change resilience and adaptation), and the effect on climate of greenhouse
gas from construction, operation and maintenance projects.",05/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Climate
Climate change resilience
Adaptation
Greenhouse gases
Assessing
Reporting
Construction
Operation
Maintenance",Active,,,,,,https://www.standardsforhighways.co.uk/search/d1ec82f3-834b-4d5f-89c6-d7d7d299dce0,,,,,,
Xf4Vz7Rd,LA 115 - Habitats Regulations assessment,https://www.standardsforhighways.co.uk/search/e2fdab58-d293-4af7-b737-b55e08e045ae,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for assessment and reporting of the implications, from
construction, operation and maintenance, of highways and/or roads projects on European sites.
These requirements accord with the relevant national legislation transposing the provisions of
Council Directive 92/43/EEC, on the conservation of natural habitats and of wild fauna and flora
(Habitats Directive), and Council Directive 2009/147/EC, on the conservation of wild birds (Birds
Directive).",06/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Habitats Regulations assessment
Maintenance
Construction
Operation
Wild fauna
Flora",Active,,,,,,https://www.standardsforhighways.co.uk/search/e2fdab58-d293-4af7-b737-b55e08e045ae,,,,,,
Up8La6Xr,LA 116 - Cultural heritage asset management plans,https://www.standardsforhighways.co.uk/search/01e6239c-c81f-4bff-b550-7155547c952a,nationalhighways,National Highways ,eng,HTML,"This document outlines the requirements to be applied to the identification, recording and
management of cultural heritage assets.",07/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Cultural heritage asset
Identification
Recording
Management",Active,,,,,,https://www.standardsforhighways.co.uk/search/01e6239c-c81f-4bff-b550-7155547c952a,,,,,,
Tc6Vy8Do,LA 120 - Environmental management plans,https://www.standardsforhighways.co.uk/search/a3a99422-41d4-4ca1-bd9e-eb89063c7134,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for the preparation and implementation of
environmental management plans for construction of highways and/or roads projects.",08/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Environmental management plans
Preparation
Implementation",Active,,,,,,https://www.standardsforhighways.co.uk/search/a3a99422-41d4-4ca1-bd9e-eb89063c7134,,,,,,
Mk7Li9Du,LD 117 - Landscape design,https://www.standardsforhighways.co.uk/search/82073bde-ec0c-4d4f-8eeb-afe0ace3c639,nationalhighways,National Highways ,eng,HTML,This document provides requirements for landscape design.,09/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Landscape design,Active,,,,,,https://www.standardsforhighways.co.uk/search/82073bde-ec0c-4d4f-8eeb-afe0ace3c639,,,,,,
Sv1Vs4Lv,LD 118 - Biodiversity design,https://www.standardsforhighways.co.uk/search/9317652b-4cb8-4aaf-be57-b96d324c8965,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for ecological survey and design of biodiversity
measures on highways projects.",10/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Biodiversity measures
Ecological survey",Active,,,,,,https://www.standardsforhighways.co.uk/search/9317652b-4cb8-4aaf-be57-b96d324c8965,,,,,,
Fw3Ja9Ve,LD 119 - Roadside environmental mitigation and enhancement,https://www.standardsforhighways.co.uk/search/6cacd1e7-dcff-4ff8-aa64-bd5556a5eedc,nationalhighways,National Highways ,eng,HTML,"This document sets out the requirements for the design of roadside environmental mitigation and
enhancement on highway projects.",11/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Roadside environmental mitigation
Enhancement",Active,,,,,,https://www.standardsforhighways.co.uk/search/6cacd1e7-dcff-4ff8-aa64-bd5556a5eedc,,,,,,
Ts4Yo6Ya,TA 101 - Traffic signalling systems,https://www.standardsforhighways.co.uk/search/html/126f775e-9890-4caf-8c1e-932f8fc949fe?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains appraisal requirements for traffic signalling systems.,12/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Traffic signalling systems
Appraisal requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/126f775e-9890-4caf-8c1e-932f8fc949fe,,,,,,
Wb4Cj7Dz,TA 121 - Ramp metering,https://www.standardsforhighways.co.uk/search/6f88abb1-4781-4360-a788-1e946a2a3797,nationalhighways,National Highways ,eng,HTML,This document contains appraisal requirements for ramp metering.,13/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Ramp metering
Appraisal requirements",Active,,,,,,https://www.standardsforhighways.co.uk/search/6f88abb1-4781-4360-a788-1e946a2a3797,,,,,,
Nx9Zr5Sq,TA 401 - Renewable energy systems appraisal,https://www.standardsforhighways.co.uk/search/html/e2a9690e-474e-4966-935e-3abc95d226c2?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains the requirements for the appraisal of new and retrofitted renewable energy system installations on motorways and all-purpose trunk roads.,14/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Renewable energy systems
Environmental measures
Appraisal
Retrofitting",Active,,,,,,https://www.standardsforhighways.co.uk/search/e2a9690e-474e-4966-935e-3abc95d226c2,,,,,,
Ga4Jg5Hv,TA 501 - Road lighting appraisal,https://www.standardsforhighways.co.uk/search/6dd9ef51-0898-474a-8680-364924145afd,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the appraisal of new and replacement road lighting
on motorways and all-purpose trunk roads.",15/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road lighting
Appraisal
Replacement lighting
New lighting",Active,,,,,,https://www.standardsforhighways.co.uk/search/6dd9ef51-0898-474a-8680-364924145afd,,,,,,
Fd1Ij6Wd,TD 131 - Roadside technology and communications,https://www.standardsforhighways.co.uk/search/html/afc9e46d-3a8e-441f-9067-15e258038d3c?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains design requirements for roadside technology and communications.,16/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Roadside technology
Roadside communications",Active,,,,,,https://www.standardsforhighways.co.uk/search/afc9e46d-3a8e-441f-9067-15e258038d3c,,,,,,
Ad4Sa3Sc,TG 411 - Electricity supply connections,https://www.standardsforhighways.co.uk/search/b6db727b-470e-4351-8778-d95350334f17,nationalhighways,National Highways ,eng,HTML,This document provides the requirements and advice for electricity supply connections.,17/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Electricity supply connections
Requirements
Advice",Active,,,,,,https://www.standardsforhighways.co.uk/search/b6db727b-470e-4351-8778-d95350334f17,,,,,,
Fe0Qz8Uh,TM 101 - Traffic signalling systems (maintenance and operation),https://www.standardsforhighways.co.uk/search/html/4f8669c0-dc84-438e-aab5-cedbcb83d629?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains maintenance and operation requirements for traffic signalling systems.,18/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Traffic signalling systems,Active,,,,,,https://www.standardsforhighways.co.uk/search/4f8669c0-dc84-438e-aab5-cedbcb83d629,,,,,,
By4Qg0Om,TM 501 - Road lighting maintenance,https://www.standardsforhighways.co.uk/search/bd9440fb-5fc5-4026-a62d-bec7b7eed99f,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the maintenance and operation of new and
replacement road lighting on motorways and all-purpose trunk roads.",19/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road lighting
Maintenance
Replacement lighting
New lighting",Active,,,,,,https://www.standardsforhighways.co.uk/search/bd9440fb-5fc5-4026-a62d-bec7b7eed99f,,,,,,
Uq6Kf6Md,TS 101 - Traffic signalling systems (inspection and assessment),https://www.standardsforhighways.co.uk/search/html/b55f5c30-b8e7-4f34-9fbf-a00d4e3cf19b?standard=DMRB,nationalhighways,National Highways ,eng,HTML,This document contains inspection and assessment requirements for traffic signalling systems.,20/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Traffic signalling systems
Inspection
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/b55f5c30-b8e7-4f34-9fbf-a00d4e3cf19b,,,,,,
Nz9Ir0De,TS 501 - Road lighting inspection,https://www.standardsforhighways.co.uk/search/e8a5043f-df60-4df3-9969-61d8e9e9fb02,nationalhighways,National Highways ,eng,HTML,"This document contains the requirements for the inspection and assessment of new and
replacement road lighting on motorways and all-purpose trunk roads.",21/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Road lighting
Inspection
Assessment",Active,,,,,,https://www.standardsforhighways.co.uk/search/e8a5043f-df60-4df3-9969-61d8e9e9fb02,,,,,,
Qd8Rf8Ke,B Series - Edge of Pavement Details,https://www.standardsforhighways.co.uk/search/c5b0ee62-6017-46bc-877f-d4ecea876db3,nationalhighways,National Highways ,eng,HTML,Edge of Pavement Details,22/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Edge of Pavement Details,Active,,,,,,https://www.standardsforhighways.co.uk/search/c5b0ee62-6017-46bc-877f-d4ecea876db3,,,,,,
Rj0Xz6Ka,C Series - Concrete Carriageway,https://www.standardsforhighways.co.uk/search/e544427b-6a9d-4c8e-a282-bf2e3e8b56fd,nationalhighways,National Highways ,eng,HTML,Concrete Carriageway,23/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Concrete Carriageway,Active,,,,,,https://www.standardsforhighways.co.uk/search/e544427b-6a9d-4c8e-a282-bf2e3e8b56fd,,,,,,
Ac0Mh1Nr,D Series - Carriageway Markings for Rural Motorways,https://www.standardsforhighways.co.uk/search/339646bb-a158-4712-b4a8-13c82aa89373,nationalhighways,National Highways ,eng,HTML,Carriageway Markings for Rural Motorways,24/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Carriageway Markings
Rural Motorways",Active,,,,,,https://www.standardsforhighways.co.uk/search/339646bb-a158-4712-b4a8-13c82aa89373,,,,,,
Wv3Po8Sa,E Series - Distance Marker Posts,https://www.standardsforhighways.co.uk/search/515b1c2d-0ac5-476f-9c6c-228f938301e2,nationalhighways,National Highways ,eng,HTML,Distance Marker Posts,25/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Distance Marker Posts,Active,,,,,,https://www.standardsforhighways.co.uk/search/515b1c2d-0ac5-476f-9c6c-228f938301e2,,,,,,
Oh4Vz7Go,F Series - Drainage,https://www.standardsforhighways.co.uk/search/61caf07a-f45c-483b-865f-4462ba6bd7eb,nationalhighways,National Highways ,eng,HTML,Drainage,26/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Drainage,Active,,,,,,https://www.standardsforhighways.co.uk/search/61caf07a-f45c-483b-865f-4462ba6bd7eb,,,,,,
Zk2Ak2Du,G Series - Loop Detectors,https://www.standardsforhighways.co.uk/search/2b9c4cbc-6341-4929-bdb9-945dbda24464,nationalhighways,National Highways ,eng,HTML,Loop Detectors,27/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Loop Detectors,Active,,,,,,https://www.standardsforhighways.co.uk/search/2b9c4cbc-6341-4929-bdb9-945dbda24464,,,,,,
Tq8Bk1Kb,H Series - Fences. Stiles and Gates,https://www.standardsforhighways.co.uk/search/c930cae4-6b41-4fbd-a90e-ab28df5ed587,nationalhighways,National Highways ,eng,HTML,Fences. Stiles and Gates,28/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,"Fences
Stiles
Gates",Active,,,,,,https://www.standardsforhighways.co.uk/search/c930cae4-6b41-4fbd-a90e-ab28df5ed587,,,,,,
Uj3Ve4Sk,I Series - Underground Cable Ducts,https://www.standardsforhighways.co.uk/search/ebdc5d20-3d2a-413b-88f4-fd53994d4665,nationalhighways,National Highways ,eng,HTML,Underground Cable Ducts,29/04/2015,09/04/2021,09/04/2021,Highways Construction Companies,GB-ENG,42110,Standards,https://www.nationalarchives.gov.uk/doc/open-government-licence/,Underground Cable Ducts,Active,,,,,,https://www.standardsforhighways.co.uk/search/ebdc5d20-3d2a-413b-88f4-fd53994d4665,,,,,,
Nd5Yh7Ug,J Series - Flexible Composite Carriageway,https://www.standardsforhighways.co.uk/search/4ff4ed85-f76a-484f-a310-f63c94912a90,nationalhighways,National Highways,eng,HTML,Drawings of flexible composite carriageways design,30/04/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,Flexible composite carriageway,Active,,,,,,,,,,,,
Uz4Vw5Bz,K Series - Miscellaneous,https://www.standardsforhighways.co.uk/search/cf01310b-1fbf-45f7-951b-e508b3bc793c,nationalhighways,National Highways,eng,HTML,Drawings of msicellaneous highways elements,01/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,Miscellaneous drawings,Active,,,,,,,,,,,,
Oc5Dm2Ty,Ground Investigation: Part 3 Model Contract Document,https://www.standardsforhighways.co.uk/search/f4d5c14f-d415-424a-8239-7d2dcd1f9e48,nationalhighways,National Highways,eng,HTML,A Model Contract for Ground Investigations,02/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investigation
Model Contract",Active,,,,,,,,,,,,
Ql7Uu8Ve,Ground Investigation: Part 4 Specification,https://www.standardsforhighways.co.uk/search/7c87758f-45df-49de-b01f-0d21183b444d,nationalhighways,National Highways,eng,HTML,A Model Specification for Ground Investigation contracts,03/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification",Active,,,,,,,,,,,,
Mi8Bh9Cy,Ground Investigation: Part 5 Notes for Guidance on the Specification for Ground Investigation,https://www.standardsforhighways.co.uk/search/9eb6b4c2-5551-4f0b-8123-dc7126470201,nationalhighways,National Highways,eng,HTML,"This Notes for Guidance should be used in conjunction
with Specification for Ground Investigation for Highway
Works. The notes provide guidance on the preparation of
the schedules to accompany the specification.",04/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investigation
Specification",Active,,,,,,,,,,,,
Qm6Wf4Ro,Ground Investigation: Part 6 Method of Measurement,https://www.standardsforhighways.co.uk/search/732e9428-f99d-487a-b5a6-d98eb7db666f,nationalhighways,National Highways,eng,HTML,"This Method of Measurement is to be used in
conjunction with the Specification for Ground
Investigation for Highway Works.",05/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Cy6Dd9Qz,Library of Standard Item Descriptions for Highway Works,https://www.standardsforhighways.co.uk/search/e64aee7d-3ed1-43c5-96b2-3ea7eb550634,nationalhighways,National Highways,eng,HTML,List of relevant descriptions for highways contracts,06/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Oq5Ow2Bd,"Method of Measurement and Bill of Quantities for Mechanical and Electrical Works in Road Tunnels, Movable Bridges and Bridge Access Gantries",https://www.standardsforhighways.co.uk/search/88e3a027-abcc-48e5-b58b-fde9c0cd1861,nationalhighways,National Highways,eng,HTML,"This Section of Volume 5 of the Manual of Contrat
Documents for Highway Works covers the procedural,
contratual and technical requirements for the mechanical
and electrical installations for road tunnels, moveable
bridges and bridge access gantries. Part 4 covers
Method of Measurement and Bills of Quantities for
Mechanical and Electrical Works in Road Tunnels,
Movable Bridges and Bridge Access Gantries",07/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Zk3Dh5Lk,Method of Measurement for Highway Works,https://www.standardsforhighways.co.uk/search/1e56dda3-cc10-4588-90be-a1e9a8a7870a,nationalhighways,National Highways,eng,HTML,"This document contains replacement pages for
incorporation into the Bills of Quantities for Highway
Works.",08/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements
Bills of Quanitities",Active,,,,,,,,,,,,
Mo9Bq5Hk,Model Contract Document for Engineering and Construction Contract - England (November 2001),https://www.standardsforhighways.co.uk/search/f4cfff89-2767-4533-8094-6d856f850ae7,nationalhighways,National Highways,eng,HTML,"This Model Contract Document gives guidance and
model documentation for use with ICE's Engineering
and Construction Contract in England. The Model
supersedes and replaces the version dated April 1999
and all subsequent amendments.",09/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Model Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Rm8Hj7Rq,Notes for Guidance on the Method of Measurement for Highway Works,https://www.standardsforhighways.co.uk/search/1cb9e50a-6bf1-4193-8f9c-3c4979d9bd30,nationalhighways,National Highways,eng,HTML,Guidance on using the Method of Measurement element of highways contracts.,10/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Model Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Ny9Td7Tc,MCX 0131 - MCX 0139 drawings,https://www.standardsforhighways.co.uk/search/a4f52851-fa6f-4ede-a7ff-e92a188b47c3,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,11/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
By2Kl0Rf,MCX 0000 - MCX 0130 drawings,https://www.standardsforhighways.co.uk/search/7a5cbac0-2c3e-471e-806e-1808d53eb5ce,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,12/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Js4Tt6Wj,MCX 0140 - MCX 0149 drawings,https://www.standardsforhighways.co.uk/search/7a5cbac0-2c3e-471e-806e-1808d53eb5ce,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,13/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Uo1Kw8Rs,MCX 0150 - MCX 0159 drawings,https://www.standardsforhighways.co.uk/search/c9c99349-0dec-4d7d-b5fe-d91950a32ddc,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,14/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Cg5Jw2Ge,MCX 0160 - MCX 0169 drawings,https://www.standardsforhighways.co.uk/search/eae56b18-bf63-4e06-bfa8-a995a1bd39bf,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,15/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Ea8Yq4Na,MCX 0170 - MCX 0305 drawings,https://www.standardsforhighways.co.uk/search/cfab0a17-6b5e-4f71-8823-46570e5c5311,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,16/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Uu7Ts2Yg,MCX 0306 - MCX 0336 drawings,https://www.standardsforhighways.co.uk/search/4a9eb51c-c8a8-4580-a0cc-ae7b1608f43e,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,17/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Rb6Ru9Mb,MCX 0337 - MCX 0425 drawings,https://www.standardsforhighways.co.uk/search/e98892e7-32ab-4df3-abbf-a76fff6c2c33,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,18/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Hv9Tz2Ew,MCX 0426 - MCX 0489 drawings,https://www.standardsforhighways.co.uk/search/872a4c29-4ce1-4aa7-9b9a-f7a85476ee72,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,19/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Kz3La3Bd,MCX 0490 - MCX 0508 drawings,https://www.standardsforhighways.co.uk/search/b88b8d8e-cd85-44d4-af9d-061b31ee94f1,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,20/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Sa3Ah1Sr,MCX 0509 - MCX 0551 drawings,https://www.standardsforhighways.co.uk/search/94a5b9d9-7d5b-4620-92a7-e46998a5a04a,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,21/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Ui8Oo8Fv,MCX 0552 - MCX 0581 drawings,https://www.standardsforhighways.co.uk/search/b789b494-ad79-4991-a94b-2b91966a75b0,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,22/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Zc4Yr1Gs,MCX 0582 - MCX 0589 drawings,https://www.standardsforhighways.co.uk/search/f078f932-b654-4ce3-aaf0-68aef483a4d5,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,23/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Jr1Od8Rg,MCX 0590 - MCX 0601 drawings,https://www.standardsforhighways.co.uk/search/715636a7-6d30-401c-ae23-9928cef9391e,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,24/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Yb2Bg9Db,MCX 0602 - MCX 0799 drawings,https://www.standardsforhighways.co.uk/search/2a462289-410d-4028-815f-15afbecbb469,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,25/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Io5Jf8Gk,MCX 0800 - MCX 0809 drawings,https://www.standardsforhighways.co.uk/search/444eddb8-1f40-42f0-9a60-c7eb772ac52a,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,26/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Az8Bl0Ps,MCX 0810 - MCX 0819 drawings,https://www.standardsforhighways.co.uk/search/cd742d7b-51e7-4a32-8e05-c6c0ac645910,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,27/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Bl4Nx5Xw,MCX 0820 - MCX 0829 drawings,https://www.standardsforhighways.co.uk/search/69efc8f1-6415-472d-806b-ba5e95ee876e,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,28/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Qg1Uj4Yt,MCX 0830 - MCX 0850 drawings,https://www.standardsforhighways.co.uk/search/bc7d0fe7-7762-4dbf-86ee-541aa1aa7cf0,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,29/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Pa7Fy4Ay,MCX 0851 - MCX 0860 drawings,https://www.standardsforhighways.co.uk/search/ccc4b3a5-9128-4d1b-ad5b-2b9ab98a1c67,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,30/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Qy2Gu4Ka,MCX 0861 - MCX 0870 drawings,https://www.standardsforhighways.co.uk/search/889a79c8-cf23-4389-8b8a-098389a40986,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,31/05/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Sb0If6Jx,MCX 0871 - MCX 1030 drawings,https://www.standardsforhighways.co.uk/search/2690cfbb-f65d-4ec0-a7fd-f04d20b8653d,nationalhighways,National Highways,eng,HTML,Technical drawings of specifications for highway contractors,01/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Technical drawings
Specification
Highways construction",Active,,,,,,,,,,,,
Ls6Ms1Ff,Notes for Guidance on the Specification of Highway Works Amendments,https://www.standardsforhighways.co.uk/search/97a04b3b-c67c-4b16-bbf3-caa32a08e961,nationalhighways,National Highways,eng,HTML,"This document contains replacement pages for
incorporation into the Notes for Guidance on the
Specification for Highway Works.",02/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Eq5Xb6Na,Specification for Highway Works Amendments,https://www.standardsforhighways.co.uk/search/b22c0193-99f5-42a4-ae35-a684d502b3b7,nationalhighways,National Highways,eng,HTML,"This document contains replacement pages for
incorporation into the Specification for Highway Works.",03/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements",Active,,,,,,,,,,,,
Zh7Gh9Fj,SA 1/08 - List of Compliant/Approved/Registered Products,https://www.standardsforhighways.co.uk/search/53c2932b-6c5a-4356-b846-e383f344f00a,nationalhighways,National Highways,eng,HTML,"This document lists products which comply with the
Traffic Signs Regulations and General Directions
(TSRGD) 2002, direction 57 or have obtained Statutory
Type Approval, Type Approval and Registration in order
that they can be used on the Highways Agency's road
network.",04/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements
Approved products",Active,,,,,,,,,,,,
Za0Gy6Uv,SA 9/97 - Ground Investigation: Part 2 Ground Investigation Procedure,https://www.standardsforhighways.co.uk/search/1b44b655-48f4-4315-947e-11629c4225de,nationalhighways,National Highways,eng,HTML,"This Advice Note complements SD 13/97,
Documentation Requirements for Ground Investigation
Contracts. It gives guidance on the planning and
execution of ground investigations for trunk roads and
motorways and gives advice on documentation.",05/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Contracts
Ground investogation
Specification
Measurements
Trunk Roads
Motorways",Active,,,,,,,,,,,,
Dk8Ir7Kr,SA 10/05 - The New Roads and Street Works Act 1991 - Diversionary Works,https://www.standardsforhighways.co.uk/search/5743f8c2-0c25-4de0-989f-f7b3bf3c3e57,nationalhighways,National Highways,eng,HTML,"This Advice Note provides guidance on the steps to be taken by the Overseeing Organisation
(OO), its agents and contractors under New Roads and Street Works Act 1991 (NRSWA) when
diversionary works may be required to apparatus owned by an Undertaker. Diversionary works
include the removal, alteration and protection of Undertakers' apparatus. Some advice is also
given where NRSWA is not applicable to the necessary diversionary works.",06/06/2015,09/04/2021,09/04/2021,Highways contractors,GB-ENG GB-WLS GB-SCT,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Road works
Diversion
Amendment",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/1991/22
https://www.legislation.gov.uk/uksi/2000/3314
https://www.legislation.gov.uk/ssi/2003/509
https://www.legislation.gov.uk/uksi/1992/1690"
Yz1Ce6Hq,SA 11/05 - The Street Works (Northern Ireland) Order 1995 - Diversionary Works,https://www.standardsforhighways.co.uk/search/a39be657-cbca-41e9-8f6a-ed80f67f5f1b,nationalhighways,National Highways,eng,HTML,"This Advice Note provides guidance on the steps to be taken by the Overseeing Organisation
(OO), its agents and contractors under New Roads and Street Works Act 1991 (NRSWA) when
diversionary works may be required to apparatus owned by an Undertaker. Diversionary works
include the removal, alteration and protection of Undertakers' apparatus. Some advice is also
given where NRSWA is not applicable to the necessary diversionary works.",07/06/2015,09/04/2021,09/04/2021,Highways contractors,GB-NIR,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Road works
Diversion
Amendment",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/nisi/1995/3210
https://www.legislation.gov.uk/nisr/1998/156"
Pv5Pb1Ap,SD 0/14 - Introduction to the Manual of Contract Documents for Highway Works (MCHW),https://www.standardsforhighways.co.uk/search/0d8a66e0-0e4a-4df1-b807-535826d0d700,nationalhighways,National Highways,eng,HTML,"This Standard introduces the Manual of Contract
Documents (MCHW). It sets out the Overseeing
Organisations' requirements for Contracts for Trunk
Roads within a structured system.",08/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"MCHW
Manual of Contract Documents
Introduction",Active,,,,,,,,,,,,
Rl7Eq5Zw,"SD 1/22 - Implementation of the Specification for Highway Works, Notes for Guidance on the Specification for Highway Works, The Highway Construction Details and the Bill of Quantities for Highway Works",https://www.standardsforhighways.co.uk/search/2f26d399-2e70-460b-9cc5-dad58542b6d4,nationalhighways,National Highways,eng,HTML,"This document replaces the existing implementation
standard for the Specification for Highway Works,
Notes for Guidance on the Specification for Highway
Works, the Highway Construction Details and the Bills
of Quantities for Highway Works.",09/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"MCHW
Manual of Contract Documents
Guidance",Active,,,,,,,,,,,,
Ns6Qo6Qy,SD 5/92 - Implementation of Model Contract Documents for Highway Works,https://www.standardsforhighways.co.uk/search/89df8525-d33c-4cf1-a925-3da9cf8a77c7,nationalhighways,National Highways,eng,HTML,"This Standard introduces the Model Contract
Document for use with the December 1991 Edition of
the Specification for Highway Works and gives
implementation requirements for its use in trunk road
contracts in the appropriate part of the UK.",10/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"MCHW
Manual of Contract Documents
Guidance
Trunk roads
Motorways",Active,,,,,,,,,,,,
Ni3Hh5Wu,SD 13/97 - Ground Investigation: Part 1 Documentation Requirements for Ground Investigation Contracts,https://www.standardsforhighways.co.uk/search/ecfabc68-062e-4e51-ad4f-eec7c1b6907f,nationalhighways,National Highways,eng,HTML,"This Standard sets out the documentation to be used for
Ground Investigation Contracts on trunk road schemes,
including motorway schemes.",11/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"MCHW
Manual of Contract Documents
Guidance
Trunk roads
Motorways
Required Documentation",Active,,,,,,,,,,,,
Cq8Ck4Sg,SD 14/00 - Implementation Standard for Trenchless Installation of Highway Drainage and Service Ducts,https://www.standardsforhighways.co.uk/search/90fcae4e-b748-427d-adf7-83a0582d2726,nationalhighways,National Highways,eng,HTML,"This Standard introduces the Specification, Notes for
Guidance, and Method of Measurement for Trenchless
Installation of Highway Drainage and Service Ducts for
trunk road contracts in the UK.",12/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"MCHW
Manual of Contract Documents
Guidance
Trunk roads
Motorways
Drainage
Service Ducts
Installation",Active,,,,,,,,,,,,
Nd1Mp4Jg,Series 000 - Introduction,https://www.standardsforhighways.co.uk/search/1dc9b4c3-4c97-4486-b0ac-ea6a9a758750,nationalhighways,National Highways,eng,HTML,"Introduction to the specification for highway works, outlining key documents and abberviations used in the series.",13/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards",Active,,,,,,,,,,,,
Os4Qi9Ll,Series 0100 - Preliminaries,https://www.standardsforhighways.co.uk/search/84bb306d-e448-4cf8-8d4d-8e1e89a5b265,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the preliminary elements of a highway contruction contract.,14/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Preliminaries",Active,,,,,,,,,,,,
Mc7Io9Oi,Series 0200 - Site Clearance,https://www.standardsforhighways.co.uk/search/fffc17fe-6862-4d69-bdc2-8e8be04b3ce3,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the site clearance of a highway contruction contract.,15/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Site clearance",Active,,,,,,,,,,,,
Si3Ve5Ge,Series 0300 - Fencing,https://www.standardsforhighways.co.uk/search/fb286ffa-84f8-42da-b7e9-9e1c68474098,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the fencing of a highway contruction contract.,16/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Fencing
Timber
Painting",Active,,,,,,,,,,,,
Xl0Ur6Lg,Series 0400 - Road Restraint Systems - Vehicle and Pedestrian,https://www.standardsforhighways.co.uk/search/3d1cb227-faf1-448c-b83e-46884fbf50d2,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the road restraint systems of a highway contruction contract.,17/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Road restraint systems
Vehicle
Pedestrian
Durability
Barriers
Vehicle Parapets
Anti-glare screens",Active,,,,,,,,,,,,
Ov0We4Jw,Series 0500 - Drainage and Service Ducts,https://www.standardsforhighways.co.uk/search/d979f80c-d69b-4a50-896f-50d7c27dcdc7,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the drainage and service ducts of a highway contruction contract.,18/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Drainage
Service Ducts
Pipes
Drains",Active,,,,,,,,,,,,
Ef7Qb2Yk,Series 0600 - Earthworks,https://www.standardsforhighways.co.uk/search/471049cb-7dd8-452a-81e6-fc8af7d31b91,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the earthworks of a highway contruction contract.,19/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Earthworks
Landscaping
Watercourse",Active,,,,,,,,,,,,
Kd2Hk3Nk,Series 0700 - Road Pavements - General,https://www.standardsforhighways.co.uk/search/673f0872-f3da-4623-963f-a49757d0039f,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the road pavements of a highway contruction contract.,20/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement",Active,,,,,,,,,,,,
Zc9Zs5Am,"Series 0800 - Road Pavements - Unbound, Cement and Other Hydraulically Bound Mixtures",https://www.standardsforhighways.co.uk/search/c7f58300-b868-43ae-819a-7b600e764000,nationalhighways,National Highways,eng,HTML,"This document sets out the standards for undertaking the unbound, cement and hydraulically bound road pavements of a highway contruction contract.",21/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Unbound
Cement
Hydraulically Bound
Aggregates",Active,,,,,,,,,,,,
Ba8Oy1Fg,Series 0900 - Road Pavements - Bituminous Bound Materials,https://www.standardsforhighways.co.uk/search/c7c905c3-bfac-4ad5-8f7d-8891ab7ca4b4,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the bituminous bound pavements of a highway contruction contract.,22/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Bituminous Bound Materials
Asphalt",Active,,,,,,,,,,,,
Gs4Pr7Nr,Series 1000 - Road Pavements - Concrete Materials,https://www.standardsforhighways.co.uk/search/ec575049-e7c8-48d1-a507-e65906706a16,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the concrete pavements of a highway contruction contract.,23/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Concrete
Roller compacted
Maintenance",Active,,,,,,,,,,,,
Pl3Zt3Iy,"Series 1100 - Kerbs, Footways, Cycleways and Paved Areas",https://www.standardsforhighways.co.uk/search/86a315ce-4061-4659-960b-8b47bc333485,nationalhighways,National Highways,eng,HTML,"This document sets out the standards for undertaking the kerbs, footways, cycleways and paved areas of a highway contruction contract.",24/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete
Roller compacted
Maintenance",Active,,,,,,,,,,,,
Jy5Ki3Op,Series 1200 - Traffic Signs,https://www.standardsforhighways.co.uk/search/31e1eb76-5906-45e5-bfa9-f024326cf9ef,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the traffic signs of a highway contruction contract.,25/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Traffic signs
Permanent
Bollards
Marker posts
Road studs
Lamps
Signals
Gantries",Active,,,,,,,,,,,,
Wr7Ss7Ui,"Series 1300 - Road Lighting Columns and Brackets, CCTV Masts and Cantilever Masts",https://www.standardsforhighways.co.uk/search/67bc7d01-0ffa-4d23-9b73-1ab11f83eda3,nationalhighways,National Highways,eng,HTML,"This document sets out the standards for undertaking the road lighting columns, CCTV masts and cantilever masts of a highway contruction contract.",26/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Road lighting
Columns
Brackets
CCTV masts
Cantilever masts",Active,,,,,,,,,,,,
Mz0Yl6Hs,Series 1400 - Electrical Work for Road Lighting and Traffic Signs,https://www.standardsforhighways.co.uk/search/30ae8a33-702b-4560-ab79-3c17bc9ac927,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the electrical work for road lighting and traffic signs of a highway contruction contract.,27/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Electrical work
Road lighting
Traffic signs
Wiring
Lamps",Active,,,,,,,,,,,,
Sx2Sv2Rr,Series 1500 - Highway Communications,https://www.standardsforhighways.co.uk/search/42aaa4f3-e6aa-48c3-9a5e-5c4dac005405,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the highway communications of a highway contruction contract.,28/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Highway communications
Cables
Gantries
Existing communications",Active,,,,,,,,,,,,
Za5Wt6Nu,Series 1600 - Piling and Embedded Retaining Walls,https://www.standardsforhighways.co.uk/search/c8b3484a-05bb-4278-98c0-10be5e5f0a67,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the piling and embedded retaining walls of a highway contruction contract.,29/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pile walls
Retaining walls",Active,,,,,,,,,,,,
Wa6Va5Tm,Series 1700 - Structural Concrete,https://www.standardsforhighways.co.uk/search/b2be331a-44e5-4efb-8eb5-111f9fbed70c,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the structural concrete of a highway contruction contract.,30/06/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete
Reinforcement
Prestressing tendons
Dowels",Active,,,,,,,,,,,,
Mz9Rq0Qj,Series 1800 - Structural Steelwork,https://www.standardsforhighways.co.uk/search/ac039ec2-c760-4d1a-9e12-31c075eb8dec,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the structural steelwork of a highway contruction contract.,01/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Strcutural steelwork
Welding
Steel
Mechanical fastening
Surface treatment",Active,,,,,,,,,,,,
Gl1Gn3Df,Series 1900 - Protection of Steelwork Against Corrosion,https://www.standardsforhighways.co.uk/search/9dd88074-8993-4e28-ab0c-a00ad4998ad9,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the protection of steelwork against corrosion of a highway contruction contract.,02/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Surface treatment
Metal coatings
Paints
Access",Active,,,,,,,,,,,,
Dl4Ti4Lt,Series 2000 - Waterproofing for Concrete Structures,https://www.standardsforhighways.co.uk/search/989e81a4-43db-4f70-afaf-774f2c16dc81,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the waterproofing for concrete structures of a highway contruction contract.,03/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Waterproofing
Bridge deck
Below ground concrete
Integrity testing",Active,,,,,,,,,,,,
Mh7Tn9Rl,Series 2100 - Bridge Bearings,https://www.standardsforhighways.co.uk/search/2b231d84-3d45-480b-8c48-6c0dd88e3007,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the bridge bearings of a highway contruction contract.,04/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bridge bearings
Corrosion
Surface preparation
Protection
Bedding mortars",Active,,,,,,,,,,,,
Mq2Cb5Ti,Series 2300 - Bridge Expansion Joints and Sealing of Gaps,https://www.standardsforhighways.co.uk/search/32d132ec-f6dd-4106-a228-e2aa8e628049,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the bridge expansion joints and sealing of gaps of a highway contruction contract.,05/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bridge deck expansion joints
Sealing of gaps
Protective treatments",Active,,,,,,,,,,,,
Mz2Hc2Kr,"Series 2400 - Brickwork, Blockwork and Stonework",https://www.standardsforhighways.co.uk/search/cf874a98-84ae-42b0-8269-0641aa59ceb8,nationalhighways,National Highways,eng,HTML,"This document sets out the standards for undertaking the brickwork, blockwork and stonework of a highway contruction contract.",06/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Brickwork
Blockwork
Stonework
Cement
Aggregates
Mortar
Stone
Protection
Bridge Masonry",Active,,,,,,,,,,,,
Iq7Cd0Uv,Series 2500 - Special Structures,https://www.standardsforhighways.co.uk/search/27aec28e-9b84-4411-9d11-14a2b8de69f1,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the special structures of a highway contruction contract.,07/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Special structures
Corrugated steel
Reinforced soil
Drainage
Rigid pipes",Active,,,,,,,,,,,,
Bq4Ax1Fg,Series 2600 - Miscellaneous,https://www.standardsforhighways.co.uk/search/7e9c0248-aaac-4c9c-9957-dc48e3de7a0d,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking miscellaneous aspects of a highway contruction contract.,08/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bedding mortar
Concrete
Plastic coating
High tensile wire
Node markers
Granolithic concrete rendering",Active,,,,,,,,,,,,
Ss4Xo5Al,Series 3000 - Landscape and Ecology,https://www.standardsforhighways.co.uk/search/50e8c0e2-638d-493f-b929-7dd4733df88a,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the landscape and ecology of a highway contruction contract.,09/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Weed control
Rabbits
Deer
Seeding
Planting
Maintenance
Trees
Shrubs
Waterbodies",Active,,,,,,,,,,,,
Nd5Go7Gb,Series 5000 - Maintenance Painting of Steelwork,https://www.standardsforhighways.co.uk/search/0f822e5a-b6aa-4033-9101-18929c0fc58f,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the maintenance painting of steelwork of a highway contruction contract.,10/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Maintenance painting
Steelwork
Surface preparation
Metal coatings
Spray coatings",Active,,,,,,,,,,,,
Wg8Fi9Vm,Series 5700 - Concrete Repairs,https://www.standardsforhighways.co.uk/search/b3f60365-847a-4fd4-abdb-747568a1c726,nationalhighways,National Highways,eng,HTML,This document sets out the standards for undertaking the concrete repairs of a highway contruction contract.,11/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete repairs
Quality control
Substrate penetration
Mortar",Active,,,,,,,,,,,,
Iz7Je7Wq,"Series 7000, 7100, 7200, 7300 - Mechanical and Electrical Installations in Road Tunnels, Movable Bridges and Bridge Access Gantries - Part 2: Standard Performance Specifications",https://www.standardsforhighways.co.uk/search/b11cf80a-2a3f-46b5-8a48-d870fa966ca7,nationalhighways,National Highways,eng,HTML,"This Section of Volume 5 of the Manual of Contrat
Documents for Highway Works covers the procedural,
contratual and technical requirements for the mechanical
and electrical installations for road tunnels, moveable
bridges and bridge access gantries.",12/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Fire safety
Safety precautions
Durability
Maintenance
Tunnels
Environmental systems",Active,,,,,,,,,,,,
Ln2Fk8Jj,Series 8000 part 2 - Trenchless Installation of Highway Drainage and Service Ducts Part 2: Specification,https://www.standardsforhighways.co.uk/search/14f15714-52ef-436f-88bf-a7a86f4700b8,nationalhighways,National Highways,eng,HTML,"This Series of the Specification applies to the
installation by trenchless techniques of highway
drainage, service ducts, sleeves and culverts of
internal diameters or width 900 mm or less.",13/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pipes
Drainage
Minimum dig techniques",Active,,,,,,,,,,,,
If4Rp2Vx,Series 8000 part 4 - Trenchless Installation of Highway Drainage and Service Ducts Part 4: Method of Measurement,https://www.standardsforhighways.co.uk/search/6fcc1e88-fb37-464e-9644-caeb82532daf,nationalhighways,National Highways,eng,HTML,"This Series of the Method of Measurement applies
to the installation by trenchless techniques of
highway drainage, service ducts, sleeves and
culverts of internal diameters or width 900 mm or
less.",14/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Standard,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Method of measurement
Drainage
Service ducts",Active,,,,,,,,,,,,
Si7El1Ev,Series NG 000 - Introduction,https://www.standardsforhighways.co.uk/search/2c441de3-5200-461e-ad02-ef3bc6a959cf,nationalhighways,National Highways,eng,HTML,Introduction to the guidance on the Specification for Highway Works.,15/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification for Highway Works
Manual of Contract Documents",Active,,,,,,,,,,,,
Jx8Mj7Kq,Series NG 0100 - Preliminaries,https://www.standardsforhighways.co.uk/search/b9dc9a3a-f787-4399-9146-3cfa4334b5c0,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the preliminary elements of a highway contruction contract.,16/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Preliminaries",Active,,,,,,,,,,,,
Jb6Ww6Kx,Series NG 0200 - Site Clearance,https://www.standardsforhighways.co.uk/search/e90a58af-f19f-480e-aed9-a74cda5ce2b9,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the site clearance of a highway contruction contract.,17/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Site clearance",Active,,,,,,,,,,,,
Jq4Cz3Rn,Series NG 0300 - Fencing,https://www.standardsforhighways.co.uk/search/3f057441-a194-424e-8a80-3d8ceb7f6a49,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the fencing of a highway contruction contract.,18/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Fencing
Timber
Painting",Active,,,,,,,,,,,,
Hq7Xx0Lh,Series NG 0400 - Road Restraint Systems - Vehicle and Pedestrian,https://www.standardsforhighways.co.uk/search/bc944939-86b5-44ae-9b1c-b4ff4d0881e4,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the road restraint systems of a highway contruction contract.,19/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Road restraint systems
Vehicle
Pedestrian
Durability
Barriers
Vehicle Parapets
Anti-glare screens",Active,,,,,,,,,,,,
Hk5Qn3Fq,Series NG 0500 - Drainage and Service Ducts,https://www.standardsforhighways.co.uk/search/0bc36cb1-2d77-45a4-b039-2f256b9628f0,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the drainage and service ducts of a highway contruction contract.,20/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Drainage
Service Ducts
Pipes
Drains",Active,,,,,,,,,,,,
Uw3Vi3Db,Series NG 0600 - Earthworks,https://www.standardsforhighways.co.uk/search/b2db98f7-2cb3-492b-996e-caf21aea22c1,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the earthworks of a highway contruction contract.,21/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Earthworks
Landscaping
Watercourse",Active,,,,,,,,,,,,
Ii7So4Kg,Series NG 0700 - Road Pavements - General,https://www.standardsforhighways.co.uk/search/746f32e9-4afe-417d-87bd-54902e2f43da,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the road pavements of a highway contruction contract.,22/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement",Active,,,,,,,,,,,,
Ye4Fx4Pq,"Series NG 0800 - Road Pavements - Unbound, Cement and Other Hydraulically Bound Mixtures",https://www.standardsforhighways.co.uk/search/54ca9d92-58bb-4844-b7e9-f9747080d3b7,nationalhighways,National Highways,eng,HTML,"This document sets out the guidance for undertaking the unbound, cement and hydraulically bound road pavements of a highway contruction contract.",23/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Unbound
Cement
Hydraulically Bound
Aggregates",Active,,,,,,,,,,,,
Yw9Bg2Vx,Series NG 0900 - Road Pavements - Bituminous Bound Materials,https://www.standardsforhighways.co.uk/search/03ff8bad-76d6-497b-b96c-086342c612e7,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the bituminous bound pavements of a highway contruction contract.,24/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Bituminous Bound Materials
Asphalt",Active,,,,,,,,,,,,
Zf3En9Rx,Series NG 1000 - Road Pavements - Concrete Materials,https://www.standardsforhighways.co.uk/search/dd6fadca-b3bb-4ecf-bbca-4652723f42bc,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the concrete pavements of a highway contruction contract.,25/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pavement
Concrete
Roller compacted
Maintenance",Active,,,,,,,,,,,,
Au6Cy8Bq,"Series NG 1100 - Kerbs, Footways, Cycleways and Paved Areas",https://www.standardsforhighways.co.uk/search/3cd42b64-7c24-470c-80ae-24dfbf857291,nationalhighways,National Highways,eng,HTML,"This document sets out the guidance for undertaking the kerbs, footways, cycleways and paved areas of a highway contruction contract.",26/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete
Roller compacted
Maintenance",Active,,,,,,,,,,,,
Zk3Ik3Dl,Series NG 1200 - Traffic Signs,https://www.standardsforhighways.co.uk/search/0152f877-0d78-49ae-8b9f-53564c14d9fb,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the traffic signs of a highway contruction contract.,27/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Traffic signs
Permanent
Bollards
Marker posts
Road studs
Lamps
Signals
Gantries",Active,,,,,,,,,,,,
Lg6Cj0Mf,"Series NG 1300 - Road Lighting Columns and Brackets, CCTV Masts and Cantilever Masts",https://www.standardsforhighways.co.uk/search/80322b2e-5c1a-4d68-bbea-aed31e6af801,nationalhighways,National Highways,eng,HTML,"This document sets out the guidance for undertaking the road lighting columns, CCTV masts and cantilever masts of a highway contruction contract.",28/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Road lighting
Columns
Brackets
CCTV masts
Cantilever masts",Active,,,,,,,,,,,,
Od5Wv0So,Series NG 1400 - Electrical Work for Road Lighting and Traffic Signs,https://www.standardsforhighways.co.uk/search/b28a80e3-58f1-407c-9ac4-157b5ac4be6a,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the electrical work for road lighting and traffic signs of a highway contruction contract.,29/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Electrical work
Road lighting
Traffic signs
Wiring
Lamps",Active,,,,,,,,,,,,
Ch1Hg2Ci,Series NG 1500 - Highway Communications,https://www.standardsforhighways.co.uk/search/d46e5475-e7c8-4b5e-a5a0-c43ce16e10c0,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the highway communications of a highway contruction contract.,30/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Highway communications
Cables
Gantries
Existing communications",Active,,,,,,,,,,,,
Xi4Yn6Tm,Series NG 1600 - Piling and Embedded Retaining Walls,https://www.standardsforhighways.co.uk/search/008eb5a9-c3cc-4e0b-aa1f-33a450ed7b33,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the piling and embedded retaining walls of a highway contruction contract.,31/07/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pile walls
Retaining walls",Active,,,,,,,,,,,,
Al9Rs1Ss,Series NG 1700 - Structural Concrete,https://www.standardsforhighways.co.uk/search/9779c245-1e26-455d-bed0-0d93e091e9d7,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the structural concrete of a highway contruction contract.,01/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete
Reinforcement
Prestressing tendons
Dowels",Active,,,,,,,,,,,,
Ga6Dw8Kg,Series NG 1800 - Structural Steelwork,https://www.standardsforhighways.co.uk/search/10b8a717-a958-4cd4-9203-c55a3d83a723,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the structural steelwork of a highway contruction contract.,02/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Strcutural steelwork
Welding
Steel
Mechanical fastening
Surface treatment",Active,,,,,,,,,,,,
Ef3Ir9Mx,Series NG 1900 - Protection of Steelwork Against Corrosion,https://www.standardsforhighways.co.uk/search/5ece9da6-1eac-411a-8573-f21153c5402f,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the protection of steelwork against corrosion of a highway contruction contract.,03/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Surface treatment
Metal coatings
Paints
Access",Active,,,,,,,,,,,,
Mz1Mk6Sr,Series NG 2000 - Waterproofing for Concrete Structures,https://www.standardsforhighways.co.uk/search/2106ba87-6b26-46e6-aa94-77c807170ef9,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the waterproofing for concrete structures of a highway contruction contract.,04/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Waterproofing
Bridge deck
Below ground concrete
Integrity testing",Active,,,,,,,,,,,,
Ec5Gr1Rr,Series NG 2100 - Bridge Bearings,https://www.standardsforhighways.co.uk/search/8d818a09-90e3-4d57-ac6c-316e73eab3fb,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the bridge bearings of a highway contruction contract.,05/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bridge bearings
Corrosion
Surface preparation
Protection
Bedding mortars",Active,,,,,,,,,,,,
Bl4Jg2Cr,Series NG 2300 - Bridge Expansion Joints and Sealing of Gaps,https://www.standardsforhighways.co.uk/search/146c0c0c-0900-425e-8030-4a04d38a0cbe,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the bridge expansion joints and sealing of gaps of a highway contruction contract.,06/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bridge deck expansion joints
Sealing of gaps
Protective treatments",Active,,,,,,,,,,,,
Ef8Ji7Vl,"Series NG 2400 - Brickwork, Blockwork and Stonework",https://www.standardsforhighways.co.uk/search/c445a05f-c959-4534-8c2b-b5ca808cb106,nationalhighways,National Highways,eng,HTML,"This document sets out the guidance for undertaking the brickwork, blockwork and stonework of a highway contruction contract.",07/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Brickwork
Blockwork
Stonework
Cement
Aggregates
Mortar
Stone
Protection
Bridge Masonry",Active,,,,,,,,,,,,
Dd2Nv0Ts,Series NG 2500 - Special Structures,https://www.standardsforhighways.co.uk/search/ca5c4a8c-e67a-429b-b401-5915a7963acc,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the special structures of a highway contruction contract.,08/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Special structures
Corrugated steel
Reinforced soil
Drainage
Rigid pipes",Active,,,,,,,,,,,,
Cr9Jk5Kr,Series NG 2600 - Miscellaneous,https://www.standardsforhighways.co.uk/search/a699bb16-9174-4860-a366-26f57737ca88,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking miscellaneous aspects of a highway contruction contract.,09/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Bedding mortar
Concrete
Plastic coating
High tensile wire
Node markers
Granolithic concrete rendering",Active,,,,,,,,,,,,
Ba8Kk9Eo,Series NG 3000 - Landscape and Ecology,https://www.standardsforhighways.co.uk/search/16ad58ff-774d-40e7-8880-7d1dc7e2a92e,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the landscape and ecology of a highway contruction contract.,10/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Weed control
Rabbits
Deer
Seeding
Planting
Maintenance
Trees
Shrubs
Waterbodies",Active,,,,,,,,,,,,
Be6Ms9Ce,Series NG 5000 - Maintenance Painting of Steelwork,https://www.standardsforhighways.co.uk/search/6937c14f-e010-4b0e-b859-ab3677872969,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the maintenance painting of steelwork of a highway contruction contract.,11/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Maintenance painting
Steelwork
Surface preparation
Metal coatings
Spray coatings",Active,,,,,,,,,,,,
Pn7Vu4Ce,Series NG 5700 - Concrete Repairs,https://www.standardsforhighways.co.uk/search/55e1b2ae-296b-42fe-9370-893972ae3a0f,nationalhighways,National Highways,eng,HTML,This document sets out the guidance for undertaking the concrete repairs of a highway contruction contract.,12/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Concrete repairs
Quality control
Substrate penetration
Mortar",Active,,,,,,,,,,,,
Eu2Nh8Ij,"Series NG 7000 - Mechanical and Electrical Installations in Road Tunnels, Movable Bridges and Bridge Access Gantries - Part 3: Notes for Guidance on the Standard Performance Specifications",https://www.standardsforhighways.co.uk/search/ae86f768-60b1-4a15-90ff-8c8e278d3ad7,nationalhighways,National Highways,eng,HTML,"This Section of Volume 5 of the Manual of Contrat
Documents for Highway Works covers the procedural,
contratual and technical requirements for the mechanical
and electrical installations for road tunnels, moveable
bridges and bridge access gantries.",13/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Fire safety
Safety precautions
Durability
Maintenance
Tunnels
Environmental systems",Active,,,,,,,,,,,,
Fb6Gl8Iu,Series NG 8000 part 3 - Trenchless Installation of Highway Drainage and Service Ducts Part 3: Notes for Guidance,https://www.standardsforhighways.co.uk/search/0e23edfa-ae27-40d9-b269-2c571de45b8d,nationalhighways,National Highways,eng,HTML,"This Series of the Specification applies to the
installation by trenchless techniques of highway
drainage, service ducts, sleeves and culverts of
internal diameters or width 900 mm or less.",14/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Specification
Highway works
Construction standards
Pipes
Drainage
Minimum dig techniques",Active,,,,,,,,,,,,
Oo8Ac0Bu,Guidance on the installation and use of scaffold guard structures over the strategic road network,https://nationalhighways.co.uk/help-centre/working-on-over-or-near-our-roads/,nationalhighways,National Highways,eng,HTML,The purpose of this document is to provide guidance on the approval process for the installation and use of scaffold guard structures over the Strategic Road Network (SRN).,15/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Strategic Road Network
SRN
Highway structures
Traffic management
Safety management
Inspection
Maintenance",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/uksi/2015/51
https://www.legislation.gov.uk/ukpga/1991/22
https://www.legislation.gov.uk/ukpga/1980/66"
Om8Ox6Dg,Planning for the future - A guide to working with National Highways on planning matters,https://nationalhighways.co.uk/media/2depj2hh/final-cre23_0370-nh-planning-guide-2023.pdf,nationalhighways,National Highways,eng,PDF,"The guide provides further advice on the information we would like to see included in a planning proposal and outlines the support we can offer at every stage of the planning process. It is aimed at development promoters and their consultants, strategic policy-making authorities, local highway authorities, sub-national transport bodies, local enterprise partnerships, community groups and others involved in development proposals which may result in any traffic or other impact on the SRN.",16/08/2015,09/04/2021,09/04/2021,"Construction companies
Planning authorities",GB,"36000
41201
41202
42110
42120
42130
42210
42220
42910
42990
43290
43999
39000
38123
38110
38120
38210
38220
39027",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Planning
Strategic Road Network
Engagement
Contruction around highways",Active,,,,,,"https://www.gov.uk/government/publications/strategic-road-network-and-the-delivery-of-sustainable-development
https://www.gov.uk/guidance/development-affecting-trunk-roads-how-local-planning-authorities-can-challenge-a-national-highways-recommendation",,,,,,https://www.legislation.gov.uk/ukpga/2015/7
Xd0Aa4Kb,"Design review at
National Highways:
A guide",https://nationalhighways.co.uk/suppliers/design-standards-and-specifications/good-design/,nationalhighways,National Highways,eng,HTML,"This guide sets out an overview of our design review process and offers practical advice to project design teams working on our schemes. It draws on 'Design Review Principles and Practice' (Design Council, 2019), and further good practice models by other expert bodies such as the Design Commission for Wales.",17/08/2015,09/04/2021,09/04/2021,"Construction planning teams
Highways contractors",GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Design
Highway design
Design review
Site visit",Active,,,,,,,,,,,,
Ra2Jh9Ht,"People, places and processes: A guide to good design at National Highways",https://nationalhighways.co.uk/suppliers/design-standards-and-specifications/good-design/,nationalhighways,National Highways,eng,HTML,"The purpose of this guide is to further the thinking about the design and quality of our roads. It supports both The road to good design (2018) and the Design Manual for Roads and Bridges standard GG103 Introduction and General Requirements for Sustainable Development and Design (2019). It gives supplementary guidance and advice to these documents, but does not constitute an instruction or requirement itself. It is a best practice guide to help designers, such as engineers, landscape architects and environmental specialists, and others such as project managers involved in the improvement and maintenance of the network, achieve better outcomes.",18/08/2015,09/04/2021,09/04/2021,Highways contractors,GB,42121,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Design principles
Highway design
Environmental responsibilities
Road safety
Ways of working",Active,,,,,,https://www.standardsforhighways.co.uk/search/89d10ef2-7833-44df-9140-df85cd6382b9,,,,,,
Ee3Hb1Bm,Designated Protected Areas,https://www.gov.uk/government/publications/designated-protected-areas,homesengland,Homes England,eng,HTML,Guidance for the provision of affordable housing in designated protected areas and local authority waiver form.,19/08/2015,09/04/2021,09/04/2021,"Developers
Local authorities",GB-ENG,"41202
41201",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Housing
House building
Designated Protected Areas
Local area",Active,,,,,,https://www.gov.uk/government/publications/designated-protected-areas,,,,,,https://www.legislation.gov.uk/uksi/2009/2098
Up4Ge7Tq,Protected Areas and leasehold enfranchisement: Explanatory note,https://www.gov.uk/government/publications/designated-protected-areas,homesengland,Homes England,eng,HTML,This note provides guidance to partners and stakeholders about Shred Ownership Leases and Right to Enfranchise regulations,20/08/2015,09/04/2021,09/04/2021,"Developers
Local authorities",GB-ENG,"41202
41201",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Housing
House building
Designated Protected Areas
Local area",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/2008/17
https://www.legislation.gov.uk/uksi/2009/2097
https://www.legislation.gov.uk/uksi/2009/2098"
Ph0Tc9Mi,Streets for a Healthy Life,https://www.gov.uk/government/publications/streets-for-a-healthy-life,homesengland,Homes England,eng,HTML,"The purpose of this document is to show what can be achieved in creating
adopted highways that are first and foremost places for people, achieving wider
benefits such as spaces for people to socialise and play, better public health,
biodiversity, reduced carbon emissions, improved water quality and slower runoff.",21/08/2015,09/04/2021,09/04/2021,"Developers
Local authorities",GB-ENG,"41202
41201",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Housing
House building
Local area
Street design
Pedestrian-friendly",Active,,https://www.gov.uk/government/publications/streets-for-a-healthy-life/streets-for-a-healthy-life-accessible-version,,,,,,,,,,
Rj8Lp0Jt,"Streets for a Healthy Life, accessible version",https://www.gov.uk/government/publications/streets-for-a-healthy-life/streets-for-a-healthy-life-accessible-version,homesengland,Homes England,eng,HTML,"The purpose of this document is to show what can be achieved in creating
adopted highways that are first and foremost places for people, achieving wider
benefits such as spaces for people to socialise and play, better public health,
biodiversity, reduced carbon emissions, improved water quality and slower runoff.",22/08/2015,09/04/2021,09/04/2021,"Developers
Local authorities",GB-ENG,"41202
41201",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Housing
House building
Local area
Street design
Pedestrian-friendly",Active,,,https://assets.publishing.service.gov.uk/media/62cd61768fa8f54e8405571e/Streets-for-a-Healthy-Life.pdf,,,,,,,,,
El0Gz0Ob,Street works qualifications in England: guidance for operatives and supervisors,https://www.gov.uk/government/publications/street-works-qualifications-in-england/street-works-qualifications-in-england-guidance-for-operatives-and-supervisors,departmentfortransport,Department for Transport,eng,HTML,The New Roads and Street Works Act 1991 (NRSWA) requires that there is a qualified operative on site at all times while street works are in progress. The qualifications held must be appropriate for the work being carried out. The act does not require all the relevant qualifications to be held by a single operative - the main requirement is that there is always at least one operative on site whose qualifications match the activities being undertaken.,23/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street Works
Street Works Qualifications Register
Certificates
Renewing",Active,,,,,,https://www.gov.uk/government/publications/safety-at-street-works-and-road-works,,,,,,
Wc7Ph0Fa,Street works permit schemes conditions,https://www.gov.uk/government/publications/street-works-permit-schemes-conditions,departmentfortransport,Department for Transport,eng,HTML,"Guidance setting out the street works permit scheme conditions that all highway authorities, imposing conditions on permits, must follow. This guidance is used with the street works permit schemes regulations guidance.",24/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB,42110,Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street Works
Street Works Qualifications Register
Certificates
Renewing
Traffic management
Working hours
Time limits
Signal usage",Active,,,,,,https://www.gov.uk/government/publications/street-works-the-2007-permit-scheme-regulations-as-amended-in-2015,,,,,,"https://www.legislation.gov.uk/uksi/2007/3372
https://www.legislation.gov.uk/uksi/2020/122
https://www.legislation.gov.uk/uksi/2022/831
https://www.legislation.gov.uk/uksi/2009/303"
Ov7Sm9Fn,Street works permit schemes,https://www.gov.uk/government/publications/street-works-permit-schemes,departmentfortransport,Department for Transport,eng,HTML,"The statutory guidance highway authorities must follow if they want to develop, vary or operate a permit scheme for street works",25/08/2015,09/04/2021,09/04/2021,Highway authorities,GB,42110,Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Highway authroity
Permits
Permit scheme",Active,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/2004/18
https://www.legislation.gov.uk/uksi/2007/3372
https://www.legislation.gov.uk/ukpga/2015/20
https://www.legislation.gov.uk/ukpga/2015/7
https://www.legislation.gov.uk/uksi/2015/958
https://www.legislation.gov.uk/uksi/2020/122
Street and Road Works (Miscellaneous Amendments) (England) Regulations 2022"
Rj6Oo2Dn,How to reinstate a road after doing street works,https://www.gov.uk/government/publications/specification-for-the-reinstatement-of-openings-in-highways,departmentfortransport,Department for Transport,eng,HTML,The standards for reinstating streets after completing street works.,26/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Openings
Highways
End of works
Excavation
Backfill
Flexible roads
Composite roads
Rigid roads
Modular roads
Footways
Cycle paths",Active,,,,,,,,,,,,https://www.legislation.gov.uk/ukpga/1991/22
Mb3Di0Mv,Street Works Act codes,https://www.gov.uk/government/publications/street-works-register/street-works-act-codes,departmentfortransport,Department for Transport,eng,HTML,How to apply for a Street Works Act (SWA) code to carry out streetworks.,27/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street Works
Code of practice",Active,,,,,,,,,,,,
Vs9Mf7Sr,Using road plates at roadworks (TAL 6/14),https://www.gov.uk/government/publications/using-road-plates-tal-614,departmentfortransport,Department for Transport,eng,HTML,Standards and guidance on using road plates to cover excavations and reduce congestion at roadworks.,28/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Road plates
Road works
Trench",,,,,,,"http://www.hse.gov.uk/pubns/books/hsg144.htm
https://www.gov.uk/government/publications/specification-for-the-reinstatement-of-openings-in-highways
",,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1991/22
http://www.legislation.gov.uk/uksi/2002/3217"
Jm8Nv4Hx,Using the core and vac technique at road works (TAL 2/14),https://www.gov.uk/government/publications/coring-and-vacuum-extraction-technique-tal-214,departmentfortransport,Department for Transport,eng,HTML,Information on using coring and vacuum extraction to open the road and repair buried equipment faster and more cost-effectively than conventional methods.,29/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Core and vac technique
Road works",,,,,,,"http://www.hse.gov.uk/pubns/books/hsg47.htm
https://www.gov.uk/government/publications/specification-for-the-reinstatement-of-openings-in-highways
http://www.hse.gov.uk/pubns/books/hsg144.htm",,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1991/22
http://www.legislation.gov.uk/uksi/2002/3217"
Oa6Ky1Pf,Using hydraulically bound mixtures at road works (TAL 3/14),https://www.gov.uk/government/publications/hydraulically-bound-mixtures-use-tal-314,departmentfortransport,Department for Transport,eng,HTML,How to use hydraulically bound mixtures in the subbase and base layers of road reinstatements and their environmental advantages.,30/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Hydraulically bound mixtures
Road works
Road reinstatements
Environmental advantages",,,,,,,"https://www.gov.uk/government/publications/specification-for-the-reinstatement-of-openings-in-highways
http://www.hse.gov.uk/pubns/books/hsg144.htm",,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1991/22
http://www.legislation.gov.uk/uksi/2002/3217"
Mp5Gf1Qz,Mapping underground assets to find buried pipes and cables (TAL 7/14),https://www.gov.uk/government/publications/mapping-underground-assets-tal-714,departmentfortransport,Department for Transport,eng,HTML,Different mapping techniques for quickly locating and identifying buried pipes and cables to be able to reduce congestion at road works.,31/08/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB,42110,Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Mapping
Undergrond assets
Street works
Road works",,,,,,,http://www.hse.gov.uk/pubns/books/hsg47.htm,,,,,,"https://www.legislation.gov.uk/uksi/2007/320
https://www.legislation.gov.uk/ukpga/1991/22
http://www.legislation.gov.uk/uksi/2002/3217"
Qv3Kj3Pg,How to record items installed under streets,https://www.gov.uk/government/publications/recording-of-underground-apparatus-in-streets-code-of-practice,departmentfortransport,Department for Transport,eng,HTML,People carrying out street works must record every item of apparatus they install underground and make these records available for inspection.,01/09/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG,42110,Statutory Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Code of practice
Underground apparatus
Street works
Road works
Recording
Excavation",,,,,,,https://www.hse.gov.uk/pubns/books/hsg47.htm,,,,,,"https://www.legislation.gov.uk/ukpga/1991/22
https://www.legislation.gov.uk/uksi/2002/3217
https://www.legislation.gov.uk/uksi/1994/3140"
Yx4Qj2Ek,Designing and modifying residential streets: Manual for streets,https://www.gov.uk/government/publications/manual-for-streets,departmentfortransport,Department for Transport,eng,HTML,"Manual for streets explains how to design, construct, adopt and maintain new and existing residential streets.",02/09/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG GB-WLS,"42110
41202",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Road works
Residential streets
Street design
Modifying streets",,,https://assets.publishing.service.gov.uk/media/5a74d26640f0b619c865ab5a/mfssummary.pdf,,,,,,,,,,
Il4Pl0Ae,Manual for streets: a summary,https://www.gov.uk/government/publications/manual-for-streets,departmentfortransport,Department for Transport,eng,HTML,"Manual for streets explains how to design, construct, adopt and maintain new and existing residential streets.",03/09/2015,09/04/2021,09/04/2021,Street works operators and supervisors,GB-ENG GB-WLS,"42110
41202",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Street works
Road works
Residential streets
Street design
Modifying streets",,,,https://assets.publishing.service.gov.uk/media/5a7e0035ed915d74e6223743/pdfmanforstreets.pdf,,,,,,,,,
Hd6Ws8Fm,Nationally significant transport infrastructure projects,https://www.gov.uk/government/publications/nationally-significant-transport-infrastructure-projects/nationally-significant-infrastructure-projects-in-the-transport-sector,departmentfortransport,Department for Transport,eng,HTML,Defines what a 'nationally significant infrastructure project' is and lists transport projects where application decisions are available.,04/09/2015,09/04/2021,09/04/2021,"Infrastructue developers
Planning authorities",GB,"42110
42120
42130
42910
42210
43999",Guidance,https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/,"Nationally significant infrastructure
Planning
Transport",,,,,,,,,,,,,"https://www.legislation.gov.uk/ukpga/2008/29
https://www.legislation.gov.uk/uksi/2013/1883/article/3/made"
"""


def get_construction_data_as_dataframe():
    # Use StringIO to convert the CSV string into a file-like object
    csv_file_like_object = StringIO(construction_data_csv)

    # Read the data into a pandas DataFrame
    df = pd.read_csv(csv_file_like_object)

    return df
