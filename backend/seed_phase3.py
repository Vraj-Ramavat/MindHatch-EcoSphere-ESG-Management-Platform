"""
Seed script for Phase 3 — Governance and Gamification data.
Run with: python manage.py shell < seed_phase3.py
"""
import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecosphere.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.models import Department, Company, Category
from governance.models import ESGPolicy, Audit, ComplianceIssue
from gamification.models import Badge, Challenge, EmployeeXP, EmployeeBadge, Reward, DepartmentScore, ChallengeParticipation

User = get_user_model()

admin_user = User.objects.filter(username='admin').first()
dept_head = User.objects.filter(username='dept_head').first()
emp1 = User.objects.filter(username='employee1').first()
emp2 = User.objects.filter(username='employee2').first()

company = Company.objects.first()

today = date.today()

# ─── ESG POLICIES ────────────────────────────────────────────────────────────
print("\n=== Creating ESG Policies ===")
policies_data = [
    {
        'title': 'Carbon Neutrality Commitment 2030',
        'description': 'This policy outlines our commitment to achieving net-zero carbon emissions by 2030 across all operations and supply chain activities.',
        'category': 'environmental',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=180),
        'review_date': today + timedelta(days=185),
    },
    {
        'title': 'Sustainable Procurement Policy',
        'description': 'Guidelines for selecting suppliers based on environmental and social responsibility criteria, ensuring our supply chain meets ESG standards.',
        'category': 'environmental',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=90),
        'review_date': today + timedelta(days=275),
    },
    {
        'title': 'Diversity, Equity & Inclusion Policy',
        'description': 'Our commitment to building an inclusive workplace that values diversity and provides equitable opportunities for all employees.',
        'category': 'social',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=365),
        'review_date': today + timedelta(days=0),
    },
    {
        'title': 'Employee Wellbeing & Mental Health Policy',
        'description': 'Framework for supporting employee mental health, work-life balance, and overall wellbeing across all departments.',
        'category': 'social',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=60),
        'review_date': today + timedelta(days=305),
    },
    {
        'title': 'Anti-Corruption & Business Ethics Code',
        'description': 'Zero-tolerance policy for bribery, corruption, and unethical business practices. All employees must complete annual training.',
        'category': 'governance',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=200),
        'review_date': today + timedelta(days=165),
    },
    {
        'title': 'Data Privacy & Information Security Policy',
        'description': 'Policy governing the collection, use, storage, and protection of personal and corporate data in compliance with GDPR and local regulations.',
        'category': 'governance',
        'priority': 'mandatory',
        'status': 'active',
        'effective_date': today - timedelta(days=120),
        'review_date': today + timedelta(days=245),
    },
    {
        'title': 'Renewable Energy Transition Roadmap',
        'description': 'Strategic plan for transitioning 100% of facility energy consumption to renewable sources by 2027.',
        'category': 'environmental',
        'priority': 'recommended',
        'status': 'active',
        'effective_date': today - timedelta(days=30),
        'review_date': today + timedelta(days=335),
    },
    {
        'title': 'Community Investment & CSR Policy',
        'description': 'Framework for allocating 2% of annual profits to community development, education, and environmental restoration programs.',
        'category': 'social',
        'priority': 'recommended',
        'status': 'draft',
        'effective_date': today + timedelta(days=30),
        'review_date': today + timedelta(days=395),
    },
]

for p in policies_data:
    policy, created = ESGPolicy.objects.get_or_create(
        title=p['title'],
        defaults={**p, 'company': company, 'created_by': admin_user}
    )
    if created:
        print(f"  Created policy: {policy.title}")

# ─── AUDITS ──────────────────────────────────────────────────────────────────
print("\n=== Creating Audits ===")
depts = list(Department.objects.all())
audits_data = [
    {
        'title': 'Annual Environmental Compliance Audit 2026',
        'audit_type': 'external',
        'auditor': 'EY Sustainability Assurance Team',
        'status': 'completed',
        'scheduled_date': today - timedelta(days=90),
        'completed_date': today - timedelta(days=75),
        'findings': 'Overall compliance rate 94%. Minor issues found in waste disposal documentation in SCM department. Energy monitoring systems require upgrade in manufacturing wing.',
        'score': 87.5,
        'department': None,
    },
    {
        'title': 'Q2 2026 Internal Carbon Footprint Audit',
        'audit_type': 'internal',
        'auditor': 'Internal ESG Committee',
        'status': 'completed',
        'scheduled_date': today - timedelta(days=45),
        'completed_date': today - timedelta(days=30),
        'findings': 'Fleet emissions 12% above target. Office energy consumption within acceptable range. Recommend accelerating EV fleet transition plan.',
        'score': 72.0,
        'department': depts[0] if depts else None,
    },
    {
        'title': 'Supply Chain Social Responsibility Audit',
        'audit_type': 'external',
        'auditor': 'Bureau Veritas',
        'status': 'in_progress',
        'scheduled_date': today - timedelta(days=15),
        'completed_date': None,
        'findings': 'Audit currently in progress. Preliminary findings show strong labour practice compliance.',
        'score': None,
        'department': depts[5] if len(depts) > 5 else None,
    },
    {
        'title': 'Q3 2026 Governance Framework Review',
        'audit_type': 'internal',
        'auditor': 'Risk & Compliance Team',
        'status': 'scheduled',
        'scheduled_date': today + timedelta(days=15),
        'completed_date': None,
        'findings': '',
        'score': None,
        'department': None,
    },
    {
        'title': 'ISO 14001 Certification Audit',
        'audit_type': 'external',
        'auditor': 'SGS Group',
        'status': 'scheduled',
        'scheduled_date': today + timedelta(days=45),
        'completed_date': None,
        'findings': '',
        'score': None,
        'department': None,
    },
]

created_audits = []
for a in audits_data:
    audit, created = Audit.objects.get_or_create(
        title=a['title'],
        defaults={**a, 'company': company}
    )
    created_audits.append(audit)
    if created:
        print(f"  Created audit: {audit.title}")

# ─── COMPLIANCE ISSUES ────────────────────────────────────────────────────────
print("\n=== Creating Compliance Issues ===")
completed_audit = next((a for a in created_audits if a.status == 'completed'), None)

issues_data = [
    {
        'title': 'Waste Disposal Documentation Gap',
        'description': 'Supply Chain department lacks proper documentation for hazardous waste disposal over the last two quarters. Records are incomplete and do not meet ISO 14001 standards.',
        'severity': 'high',
        'status': 'in_progress',
        'department': depts[5] if len(depts) > 5 else None,
        'audit': completed_audit,
        'due_date': today + timedelta(days=14),
        'assigned_to': dept_head,
    },
    {
        'title': 'Energy Monitoring System Upgrade Required',
        'description': 'Current energy monitoring infrastructure in the manufacturing wing is outdated. Real-time monitoring is not available, making accurate scope 2 emissions reporting impossible.',
        'severity': 'medium',
        'status': 'open',
        'department': depts[1] if len(depts) > 1 else None,
        'audit': completed_audit,
        'due_date': today + timedelta(days=60),
        'assigned_to': admin_user,
    },
    {
        'title': 'Fleet Emissions Exceeding Q2 Target by 12%',
        'description': 'Company fleet carbon emissions are 12% above the set Q2 target. Root cause identified as delayed EV procurement and increased sales team travel.',
        'severity': 'medium',
        'status': 'in_progress',
        'department': depts[1] if len(depts) > 1 else None,
        'audit': created_audits[1] if len(created_audits) > 1 else None,
        'due_date': today + timedelta(days=30),
        'assigned_to': dept_head,
    },
    {
        'title': 'Annual DEI Training Completion Rate Below 80%',
        'description': 'Only 67% of employees have completed the mandatory annual Diversity, Equity & Inclusion training by the deadline. Policy requires 100% completion.',
        'severity': 'low',
        'status': 'open',
        'department': depts[2] if len(depts) > 2 else None,
        'audit': None,
        'due_date': today + timedelta(days=7),
        'assigned_to': dept_head,
    },
    {
        'title': 'Supplier ESG Questionnaire Response Rate 43%',
        'description': 'Only 43% of tier-1 suppliers have responded to the annual ESG questionnaire. Minimum response rate of 75% is required for compliance reporting.',
        'severity': 'high',
        'status': 'open',
        'department': depts[5] if len(depts) > 5 else None,
        'audit': None,
        'due_date': today + timedelta(days=21),
        'assigned_to': admin_user,
    },
    {
        'title': 'Water Usage Reporting Discrepancy',
        'description': 'Discrepancy of 8.3% found between operations-reported water usage and utility bill data for Q1. Reconciliation and corrective reporting required.',
        'severity': 'low',
        'status': 'resolved',
        'department': depts[1] if len(depts) > 1 else None,
        'audit': completed_audit,
        'due_date': today - timedelta(days=10),
        'resolved_date': today - timedelta(days=5),
        'assigned_to': emp1,
    },
]

for i in issues_data:
    issue, created = ComplianceIssue.objects.get_or_create(
        title=i['title'],
        defaults={**i, 'company': company}
    )
    if created:
        print(f"  Created compliance issue: {issue.title}")

# ─── BADGES ───────────────────────────────────────────────────────────────────
print("\n=== Creating Badges ===")
badges_data = [
    {'title': 'Green Starter', 'description': 'Earned 100+ XP on sustainability activities.', 'icon': 'leaf', 'color': '#22c55e', 'unlock_rule': {'type': 'xp_threshold', 'value': 100}},
    {'title': 'Eco Warrior', 'description': 'Earned 500+ XP — a true sustainability champion!', 'icon': 'shield', 'color': '#16a34a', 'unlock_rule': {'type': 'xp_threshold', 'value': 500}},
    {'title': 'Sustainability Legend', 'description': 'Earned 1000+ XP. An inspiration to the entire organisation.', 'icon': 'trophy', 'color': '#f59e0b', 'unlock_rule': {'type': 'xp_threshold', 'value': 1000}},
    {'title': 'Challenge Rookie', 'description': 'Completed your first sustainability challenge.', 'icon': 'zap', 'color': '#3b82f6', 'unlock_rule': {'type': 'challenges_completed', 'value': 1}},
    {'title': 'Challenge Champion', 'description': 'Completed 3 or more sustainability challenges.', 'icon': 'award', 'color': '#8b5cf6', 'unlock_rule': {'type': 'challenges_completed', 'value': 3}},
    {'title': 'Community Hero', 'description': 'Participated in 3+ approved CSR activities.', 'icon': 'heart', 'color': '#ef4444', 'unlock_rule': {'type': 'csr_participations', 'value': 3}},
    {'title': 'Carbon Cutter', 'description': 'Completed the Green Commute challenge.', 'icon': 'wind', 'color': '#06b6d4', 'unlock_rule': {'type': 'challenges_completed', 'value': 1}},
    {'title': 'Water Guardian', 'description': 'Completed a Water Conservation challenge.', 'icon': 'droplets', 'color': '#0ea5e9', 'unlock_rule': {'type': 'challenges_completed', 'value': 1}},
]

created_badges = []
for b in badges_data:
    badge, created = Badge.objects.get_or_create(
        title=b['title'],
        defaults={**b, 'company': company}
    )
    created_badges.append(badge)
    if created:
        print(f"  Created badge: {badge.title}")

# ─── REWARDS ──────────────────────────────────────────────────────────────────
print("\n=== Creating Rewards ===")
rewards_data = [
    {'title': 'Extra Day Off', 'description': 'Redeem for one extra paid day off to recharge and reconnect with nature.', 'xp_cost': 500, 'stock': 20, 'icon': 'calendar'},
    {'title': 'Eco-Friendly Water Bottle', 'description': 'A premium stainless steel insulated water bottle branded with our sustainability pledge.', 'xp_cost': 150, 'stock': 50, 'icon': 'droplets'},
    {'title': 'Plant a Tree in Your Name', 'description': 'We will plant a tree in a reforestation project and send you a certificate.', 'xp_cost': 100, 'stock': 200, 'icon': 'tree-pine'},
    {'title': 'Organic Lunch Voucher', 'description': 'A lunch voucher for use at our partnered organic cafeteria. Eat well, live green.', 'xp_cost': 75, 'stock': 100, 'icon': 'utensils'},
    {'title': 'Green Skills Online Course', 'description': 'Access to a premium sustainability or ESG certification course on Coursera or LinkedIn Learning.', 'xp_cost': 300, 'stock': 30, 'icon': 'graduation-cap'},
    {'title': 'EV Charging Station Credit', 'description': 'Credit for 1 month of free EV charging at the office charging station.', 'xp_cost': 200, 'stock': 15, 'icon': 'zap'},
    {'title': 'Donation to a Green Charity', 'description': 'We will make a £50 donation to your chosen environmental charity in your name.', 'xp_cost': 250, 'stock': 100, 'icon': 'heart'},
    {'title': 'Branded Sustainability Hoodie', 'description': 'A high-quality hoodie made from 100% recycled materials with our ESG pledge logo.', 'xp_cost': 400, 'stock': 25, 'icon': 'shirt'},
]

for r in rewards_data:
    reward, created = Reward.objects.get_or_create(
        title=r['title'],
        defaults={**r, 'company': company}
    )
    if created:
        print(f"  Created reward: {reward.title}")

# ─── CHALLENGES ───────────────────────────────────────────────────────────────
print("\n=== Creating Challenges ===")
challenge_categories = {cat.name: cat for cat in Category.objects.filter(type='challenge')}

challenges_data = [
    {
        'title': 'Green Commute Month',
        'description': 'Cycle, walk, use public transport, or carpool to work every day this month. Track your sustainable commute and earn XP for every green trip!',
        'status': 'active',
        'xp_reward': 200,
        'start_date': today - timedelta(days=10),
        'end_date': today + timedelta(days=20),
        'target_value': 20,
        'target_unit': 'days',
        'max_participants': 200,
        'category': challenge_categories.get('Green Commute'),
    },
    {
        'title': 'Zero Waste Week',
        'description': 'Commit to a zero-waste lifestyle for one full week. Document waste reduction activities, bring reusable containers, and avoid single-use plastics.',
        'status': 'active',
        'xp_reward': 150,
        'start_date': today - timedelta(days=3),
        'end_date': today + timedelta(days=4),
        'target_value': 7,
        'target_unit': 'days',
        'max_participants': 150,
        'category': challenge_categories.get('Waste Reduction'),
    },
    {
        'title': 'Energy Saving Sprint',
        'description': 'Reduce your department\'s energy consumption by 10% over the next 3 weeks. Turn off lights, unplug devices, and optimise PC power settings.',
        'status': 'active',
        'xp_reward': 300,
        'start_date': today - timedelta(days=7),
        'end_date': today + timedelta(days=14),
        'target_value': 10,
        'target_unit': '% reduction',
        'max_participants': 100,
        'category': challenge_categories.get('Energy Saving'),
    },
    {
        'title': 'Water Conservation Challenge',
        'description': 'Log daily water-saving actions for 14 days — shorter showers, fixing leaks, using water-efficient appliances. Every action counts!',
        'status': 'completed',
        'xp_reward': 175,
        'start_date': today - timedelta(days=60),
        'end_date': today - timedelta(days=46),
        'target_value': 14,
        'target_unit': 'days',
        'max_participants': 100,
        'category': challenge_categories.get('Water Conservation'),
    },
    {
        'title': 'Recycling Champions',
        'description': 'Properly sort and recycle at least 5kg of materials over one month. Learn what can and cannot be recycled and share tips with your team.',
        'status': 'draft',
        'xp_reward': 125,
        'start_date': today + timedelta(days=7),
        'end_date': today + timedelta(days=37),
        'target_value': 5,
        'target_unit': 'kg recycled',
        'max_participants': 200,
        'category': challenge_categories.get('Recycling'),
    },
]

created_challenges = []
for c in challenges_data:
    challenge, created = Challenge.objects.get_or_create(
        title=c['title'],
        defaults={**c, 'company': company, 'created_by': admin_user}
    )
    created_challenges.append(challenge)
    if created:
        print(f"  Created challenge: {challenge.title}")

# ─── EMPLOYEE XP & BADGES ─────────────────────────────────────────────────────
print("\n=== Creating Employee XP & Badges ===")
xp_data = [
    (admin_user, 1250, 3),
    (dept_head, 820, 2),
    (emp1, 450, 1),
    (emp2, 275, 1),
]
for user, xp, level in xp_data:
    if user:
        xp_record, created = EmployeeXP.objects.get_or_create(
            employee=user,
            defaults={'company': company, 'total_xp': xp, 'level': level}
        )
        if not created:
            xp_record.total_xp = xp
            xp_record.level = level
            xp_record.save()
        print(f"  XP set for {user.username}: {xp} XP (Level {level})")

# Award some badges
badge_awards = [
    (admin_user, 'Sustainability Legend'),
    (admin_user, 'Challenge Champion'),
    (admin_user, 'Community Hero'),
    (dept_head, 'Eco Warrior'),
    (dept_head, 'Challenge Rookie'),
    (emp1, 'Green Starter'),
    (emp1, 'Challenge Rookie'),
    (emp2, 'Green Starter'),
]
for user, badge_title in badge_awards:
    if user:
        badge = Badge.objects.filter(title=badge_title).first()
        if badge:
            eb, created = EmployeeBadge.objects.get_or_create(employee=user, badge=badge, defaults={'company': company})
            if created:
                print(f"  Awarded badge '{badge_title}' to {user.username}")

# ─── CHALLENGE PARTICIPATIONS ─────────────────────────────────────────────────
print("\n=== Creating Challenge Participations ===")
active_challenges = [c for c in created_challenges if c.status == 'active']
if emp1 and active_challenges:
    for ch in active_challenges[:2]:
        ChallengeParticipation.objects.get_or_create(
            challenge=ch, employee=emp1,
            defaults={'company': company, 'progress': random.uniform(30, 70), 'status': 'active'}
        )
        print(f"  emp1 joined: {ch.title}")

if emp2 and active_challenges:
    ChallengeParticipation.objects.get_or_create(
        challenge=active_challenges[0], employee=emp2,
        defaults={'company': company, 'progress': random.uniform(10, 50), 'status': 'active'}
    )
    print(f"  emp2 joined: {active_challenges[0].title}")

# ─── DEPARTMENT LEADERBOARD SCORES ───────────────────────────────────────────
print("\n=== Creating Department Scores (Leaderboard) ===")
dept_scores = [
    ('ENG', 78.5, 82.0, 85.0, 81.5),
    ('OPS', 65.0, 70.0, 72.0, 68.5),
    ('HR', 72.0, 88.0, 79.0, 79.0),
    ('FIN', 68.0, 74.0, 90.0, 76.5),
    ('MKT', 60.0, 80.0, 75.0, 71.5),
    ('SCM', 55.0, 66.0, 70.0, 63.5),
    ('R&D', 80.0, 76.0, 82.0, 79.5),
]

period = date(today.year, today.month, 1)
for code, e_score, s_score, g_score, total in dept_scores:
    dept = Department.objects.filter(code=code).first()
    if dept:
        ds, created = DepartmentScore.objects.get_or_create(
            department=dept, period=period,
            defaults={
                'company': company,
                'environmental_score': e_score,
                'social_score': s_score,
                'governance_score': g_score,
                'total_score': total,
            }
        )
        if created:
            print(f"  Created score for {dept.name}: {total}/100")

print("\n✅ Phase 3 seed complete! Governance & Gamification data loaded.")
