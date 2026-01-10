# Risk Assessments used to test the accuracy of LLM prompts

import numpy as np

try:
    from .RiskAssessment import RiskAssessmentWithoutNumberInputs, RiskAssessment
except ImportError:
    from .RiskAssessment import RiskAssessmentWithoutNumberInputs, RiskAssessment

RA_empty_input = RiskAssessmentWithoutNumberInputs(
    activity="",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='',
    risk_domain="physical risk to individuals"
)

RA_controlled_likelihood_wrong_type = RiskAssessment(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='',
    risk_domain="physical risk to individuals",
    uncontrolled_likelihood='1',
    uncontrolled_severity='1',
    uncontrolled_risk='1',
    controlled_likelihood='One',
    controlled_severity='1',
    controlled_risk='1'
)

RA_mitigation_wrong_type = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room",
    mitigation="1",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='',
    risk_domain="physical risk to individuals"
)

RA_incorrect_prevention_and_mitigation = RiskAssessmentWithoutNumberInputs(
    activity="Welding metal structures",
    hazard="Exposure to toxic welding fumes",
    how_it_harms="Inhaling welding fumes can lead to respiratory problems, lung damage, and long-term health issues.",
    who_it_harms="Welders and individuals in the vicinity of the welding area.",
    prevention="Using the welding equipment in an enclosed space without proper ventilation.",
    mitigation='Get a dog with rabies to lick the wound',
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

RA_trombone_impact = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Impact from instrument",
    who_it_harms="Audience",
    how_it_harms="Slide could hit audience member, causing impact injury.",
    prevention="Keep safe distance between the player and audience",
    mitigation="Apply first aid on the injured area",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_hearing_damage = RiskAssessmentWithoutNumberInputs(
    activity="Using a trombone as a demonstration for a TPS presentation",
    hazard="Loud noise",
    who_it_harms="Everyone present",
    how_it_harms="Loud noise from instrument can cause hearing damage.",
    prevention="Play quietly, at a volume suitable for the room", # reduces likelihood of loud noise
    mitigation="Keep a space between the player and audience", # reduces severity of loud noise
    prevention_prompt_expected_class='prevention', 
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

# RA_3_water_from_instrument = RiskAssessmentWithoutNumberInputs(
#     activity="Using a trombone as a demonstration for a TPS presentation",
#     hazard="Water from instrument",
#     who_it_harms="Audience",
#     how_it_harms="Condensation formed in instrument could spread germs if released",
#     prevention="Ensure water is not released during presentation", # Not very specific.
#     # Should include feedback stating: "How would you ensure water is not released during presentation?"
#     mitigation="Keep a space between the player and audience", # Reduces severity of water being released
#     prevention_prompt_expected_class='prevention',
#     mitigation_prompt_expected_class='prevention', # reduces likelihood that someone becomes ill
#   risk_domain="physical risk to individuals"
# )

RA_ink_spill_in_eye = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Serious eye damage",
    prevention="Wear safety glasses", # If ink gets on face, wearing safety glasses reduces severity
    mitigation="Wash your eyes with clean water", # reduces severity after hazard has occurred
    prevention_prompt_expected_class='mitigation',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_ink_spill_in_eye__neither = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Serious eye damage",
    prevention="Wear gloves", # If ink gets on face, wearing safety glasses reduces severity
    mitigation="Direct more ink into the eye area", # reduces severity after hazard has occurred
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

# RA_ink_spill_in_eye_with_first_aid = RiskAssessmentWithoutNumberInputs(
#     activity="Fluids laboratory",
#     hazard="Ink spillage",
#     who_it_harms="Students",
#     how_it_harms="Serious eye damage",
#     prevention="Wear safety glasses", # reduces likelihood of hazard occurring
#     mitigation="First aid", # reduces severity after hazard has occurred
#     prevention_prompt_expected_class='mitigation',
#     mitigation_prompt_expected_class='mitigation',
# )

RA_ink_spill_in_eye_with_incorrect_how_it_harms = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Ink spillage",
    who_it_harms="Students",
    how_it_harms="Radiation exposure",
    prevention="Wear safety glasses", # reduces likelihood of hazard occurring
    mitigation="Wash your eyes with clean water", # reduces severity after hazard has occurred
    prevention_prompt_expected_class='mitigation',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_wet_hands_electric_shock = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    prevention="Students should make sure they touch electronics only with dry hands", # reduces likelihood of hazard occurring
    mitigation="Call for urgent medical assistance", # reduces severity after hazard has occurred
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_wet_hands_electric_shock__neither = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Wet hands",
    who_it_harms="Students",
    how_it_harms="Electric shock of students when touching electronics (pump power supply) with wet hands",
    prevention="Students should make sure they touch electronics only with wet hands", # reduces likelihood of hazard occurring
    mitigation="Avoid calling for urgent medical assistance", # reduces severity after hazard has occurred
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

RA_water_tank = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Water being spilt on the floor",
    who_it_harms="Students",
    how_it_harms="Injuries caused by possible slipping on wet floor",
    prevention="Do not move the water tank when it is full",
    mitigation="""If someone gets injured due to slipping, apply an ice pack to the injured area and 
    seek medical advice without delay.""",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_water_tank__neither = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Water being spilt on the floor",
    who_it_harms="Students",
    how_it_harms="Injuries caused by possible slipping on wet floor",
    prevention="Move the water tank when it is full",
    mitigation="Avoid calling for urgent medical assistance",
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

RA_syringe_needle = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    prevention="Point needle away from yourself and others",
    mitigation="Apply first aid to the affected area",
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)   

RA_syringe_needle__neither = RiskAssessmentWithoutNumberInputs(
    activity="Fluids laboratory",
    hazard="Syringes with sharp needles",
    who_it_harms="Students",
    how_it_harms="Sharp needles can pierce the skin and cause bleeding",
    prevention="Direct needle at others",
    mitigation="Wear shorts", # This is both prevention and mitigation
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

# RA_9 = RiskAssessmentWithoutNumberInputs(
#     activity="Fluids laboratory",
#     hazard="Electrocution",
#     who_it_harms="Students",
#     how_it_harms="Electrocuted by mains voltage", # This is a description of the process not the harm on the students
#     prevention="Pump plug stays away from water",
#     mitigation="First aid on site", # There needs to be a description of how this will be used in the event of an electrocution.
#     prevention_prompt_expected_class='prevention',
#     mitigation_prompt_expected_class='mitigation',
# )

# RA_13 = RiskAssessmentWithoutNumberInputs(
#     activity='Presentation Demonstration',
#     hazard='Demonstration with ruler, styrofoam and bbq sticks. I will be flicking the ruler while clamping it to a table. The bbq sticks will be stuck in the styrofoam and I will shake to show resonance',
#     who_it_harms='Me and audience',
#     how_it_harms='Could hit someone or the demonstration falls apart',
#     prevention='Do the demonstration with care',
#     mitigation='',
#     prevention_prompt_expected_class='prevention',
#     mitigation_prompt_expected_class='',
# )

RA_paper_plane_impact = RiskAssessmentWithoutNumberInputs(
    activity='Using  paper plane models as a demonstration for a TPS presentation',
    hazard='Plane could hit audience member,',
    who_it_harms='Audience',
    how_it_harms='Impact injury.',
    prevention='Throw the paper plane to a direction without anyone',
    mitigation='Apply first aid on the injured area',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_climbing_gear_on_feet = RiskAssessmentWithoutNumberInputs(
    activity='TPS presentation',
    hazard='Climbing Protection Gear (Cams and Hexs)',
    who_it_harms="Students and other individuals who would like to see how they work.",
    how_it_harms="Some equipment is heavy so could hurt if dropped on feet.",
    prevention='Inform those who wish to hold the equipment of the risk and demonstrate how they are used correctly.',
    mitigation='First aid if necessary',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_sharp_drone_propeller_blade = RiskAssessmentWithoutNumberInputs(
    activity='Bringing in a drone and two empty Li-Po batteries',
    hazard='Sharp Edge of propellor blade on drone',
    who_it_harms='Whoever pokes the propellor blade at the tip',
    how_it_harms='Is sharp to the touch to cause pain but not sharp enough to pierce skin',
    prevention='Make them aware the tip is sharp',
    mitigation='Apply a plaster if necessary',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_battery_causes_fire = RiskAssessmentWithoutNumberInputs(
    activity='Bringing in a drone and two empty Li-Po batteries',
    hazard='Li-Po battery to handle',
    who_it_harms='Whoever is holding it',
    how_it_harms='It may heat up with an unlikely chance of a fire',
    prevention='Li-Po batteries have been discharged to a safe level',
    mitigation='Li-Po batteries held in a fire-resistant bag',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_battery_causes_fire__neither = RiskAssessmentWithoutNumberInputs(
    activity='Bringing in a drone and two empty Li-Po batteries',
    hazard='Li-Po battery to handle',
    who_it_harms='Whoever is holding it',
    how_it_harms='It may heat up with an unlikely chance of a fire',
    prevention='Li-Po batteries have been discharged to an unsafe level',
    mitigation='Li-Po batteries placed in a flammable bag',
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

RA_heavy_weight_falls_on_demonstrator = RiskAssessmentWithoutNumberInputs(
    activity='Using a spring contraption as a demonstration for a TPS presentation',
    hazard='Slippage of weight from contraption',
    who_it_harms='Demonstrator',
    how_it_harms='Heavy impact when falling onto demonstator, causing injury',
    prevention='Make sure the weight is properly secured to the contraption',
    mitigation='Keep away from below the contraption',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='prevention',
    risk_domain="physical risk to individuals"
)

RA_zip_tie_hits_audience = RiskAssessmentWithoutNumberInputs(
    activity='Using a spring contraption as a demonstration for a TPS presentation',
    hazard='Cut Zip tie may fly',
    who_it_harms='Audience',
    how_it_harms='When cut the zip tie may hit an audience member',
    prevention='Keep hand around zip tie when cutting to stop it from flying',
    mitigation='Ensure safe distance between contraption and audience.',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='prevention', # Another prevention measure as it reduces the likelihood of the zip tie hitting an audience member
    risk_domain="physical risk to individuals"
)

RA_pencil_lead_projectile = RiskAssessmentWithoutNumberInputs(
    activity='Using a mechanical pencil and breaking the pencil lead against a surface for demonstration',
    hazard='Pencil lead breaking and becoming a projectile',
    who_it_harms='Anyone present',
    how_it_harms='May enter one\'s eye',
    prevention='Keep safe distance between the audience when demonstrating lead breakage',
    mitigation='Apply first aid if necessary',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

# RA = RiskAssessmentWithoutNumberInputs(
#     activity = "",
#     hazard = "",
#     how_it_harms = "",
#     who_it_harms = "",
#     prevention = "",
#     mitigation = "",
#     prevention_prompt_expected_class = "",
#     mitigation_prompt_expected_class = "",
# )

RA_fire_alarm = RiskAssessmentWithoutNumberInputs(
    activity = "Lesson in school building",
    hazard = "Smoking causes fire",
    who_it_harms = "Students and teachers",
    how_it_harms = "Burns",
    prevention = "Banning smoking in the school",
    mitigation = "Fire alarm",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)   

RA_mop_up_spill = RiskAssessmentWithoutNumberInputs(
    activity = "Fluid lab",
    hazard = "Water spills",
    how_it_harms = "Slip",
    who_it_harms = "Users",
    prevention = "Be careful",
    mitigation = "Mop up",
    prevention_prompt_expected_class = "neither", # Not specific enough
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
)

RA_mop_up_spill_correct_hazard_event_and_harm_caused = RiskAssessmentWithoutNumberInputs(
    activity = "Fluid lab",
    hazard = "Student slipping after water spilled",
    how_it_harms = "Injury caused by student slipping",
    who_it_harms = "Users",
    prevention = "Be careful",
    mitigation = "Mop up",
    prevention_prompt_expected_class = "neither", # Not specific enough
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
)

RA_syringe_with_cover = RiskAssessmentWithoutNumberInputs(
    activity = "Using syringe for injecting fuel",
    hazard = "Stabbing yourself",
    how_it_harms = "Sharp blade cuts skin and causes bleeding",
    who_it_harms = "The user",
    prevention = "Use a cover over the syringe when not in use",
    mitigation = "Wear gloves",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)

RA_hot_water_in_cups = RiskAssessmentWithoutNumberInputs(
    activity = "HEAT TRANSFER LAB",
    hazard = "Boiling (hot) water",
    how_it_harms = "Burns",
    who_it_harms = "Students",
    prevention = "Sealed cups",
    mitigation = "Cold water tap nearby",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)

RA_bigger_beaker = RiskAssessmentWithoutNumberInputs(
    activity = "Fluids Laboratory",
    hazard = "Spilling hot water on your hands",
    how_it_harms = "Leaves you with painful burn scars",
    who_it_harms = "Students",
    prevention = "Place the beaker in the middle of the table when not using it",
    mitigation = "Seal the beaker when not using it",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
)

RA_cycling_high_viz = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Collision with car",
    how_it_harms = "Impact injury",
    who_it_harms = "Cyclist",
    prevention = "Wearing a helmet",
    mitigation = "Wearing a high visibility jacket",
    prevention_prompt_expected_class = "mitigation",
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
)

RA_cycling_high_viz__neither = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Wear non reflective clothing",
    mitigation = "Wear a t-shirt",
    prevention_prompt_expected_class = "neither",
    mitigation_prompt_expected_class = "neither",
    risk_domain="physical risk to individuals"
)

RA_mucking_out_horse = RiskAssessmentWithoutNumberInputs(
    activity='Mucking out a horse',
    hazard='Horse kicks out',
    who_it_harms='Horse rider',
    how_it_harms='Impact injury',
    prevention='Keep a safe distance from the horse',
    mitigation='Wear a helmet and body protector',
    prevention_prompt_expected_class='prevention',
    mitigation_prompt_expected_class='mitigation',
    risk_domain="physical risk to individuals"
)

RA_mucking_out_horse__neither = RiskAssessmentWithoutNumberInputs(
    activity='Mucking out a horse',
    hazard='Horse kicks out',
    who_it_harms='Horse rider',
    how_it_harms='Impact injury',
    prevention='Stand directly behind the horse',
    mitigation='Wear gloves',
    prevention_prompt_expected_class='neither',
    mitigation_prompt_expected_class='neither',
    risk_domain="physical risk to individuals"
)

RA_slitter_machine = RiskAssessmentWithoutNumberInputs(
    activity="Slitter machine usage",
    hazard="Sharp blade",
    who_it_harms="Operator",
    how_it_harms="Cut hazard",
    prevention="Guard",
    mitigation="Metal gloves for maintenance",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_campfire = RiskAssessmentWithoutNumberInputs(
    activity="Building a campfire",
    hazard="Flame",
    who_it_harms="People or property",
    how_it_harms="Burns or damage",
    prevention="Safe distance from fire to be adhered to",
    mitigation="Flameproof clothing/insulation",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_campfire__neither = RiskAssessmentWithoutNumberInputs(
    activity="Building a campfire",
    hazard="Flame",
    who_it_harms="People or property ",
    how_it_harms="Burns or damage",
    prevention="Stand close to the fire",
    mitigation="Wear a hat",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="physical risk to individuals"
)

RA_bouldering = RiskAssessmentWithoutNumberInputs(
    activity="Climbing (Bouldering)",
    hazard="Not landing Safely",
    who_it_harms="Climbers",
    how_it_harms="Landing in a awkward way can cause injury",
    prevention="Make sure to climb down before you come off the wall",
    mitigation="Make sure to always land of two feet",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="prevention",
    risk_domain="physical risk to individuals"
)

RA_bouldering__neither = RiskAssessmentWithoutNumberInputs(
    activity="Climbing (Bouldering)",
    hazard="Not landing Safely",
    who_it_harms="Climbers",
    how_it_harms="Landing in a awkward way can cause injury",
    prevention="Jump off the wall",
    mitigation="Land on one foot",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="physical risk to individuals"
)

RA_hob_burn = RiskAssessmentWithoutNumberInputs(
    activity="Cooking",
    hazard="Fire/heat",
    who_it_harms="Chef",
    how_it_harms="Burns",
    prevention="Use induction stove",
    mitigation="Wear insulated gloves",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_hob_burn__neither = RiskAssessmentWithoutNumberInputs(
    activity="Cooking",
    hazard="Fire/ heat",
    who_it_harms="Chef",
    how_it_harms="Burns",
    prevention="Use gas stove",
    mitigation="Wearing no gloves",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="physical risk to individuals"
)

RA_crossing_road = RiskAssessmentWithoutNumberInputs(
    activity="Crossing Exhibition Road",
    hazard="A car crashing into you",
    who_it_harms="The person crossing the road",
    how_it_harms="Could cause potentially life threatening injury",
    prevention="Look left and right before crossing the road",
    mitigation="Call the emergency services",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_cycling = RiskAssessmentWithoutNumberInputs(
    activity="Cycle commuting",
    hazard="Head injury",
    who_it_harms="Cyclist",
    how_it_harms="Mistakes by cyclists or motorists leading to crash",
    prevention="Wear a helmet",
    mitigation="Immediately call the emergency services",
    prevention_prompt_expected_class="mitigation",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_ladder = RiskAssessmentWithoutNumberInputs(
    activity="Climbing a tall ladder",
    hazard="Falling, slipping",
    who_it_harms="the person on the ladder, people below the ladder",
    how_it_harms="The impact of hitting the ground",
    prevention="Have someone hold the ladder. Make sure the ladder is locked and the ground in even. ",
    mitigation="Wear helment and padded clothes.",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="physical risk to individuals"
)

RA_stable_ladder = RiskAssessmentWithoutNumberInputs(
    activity="Going up a ladder",
    hazard="Dangerous height",
    who_it_harms="Person climbing",
    how_it_harms="Falling",
    prevention="Someone hold ladder",
    mitigation="Buy stable ladder",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="prevention",
    risk_domain="physical risk to individuals"
)

RA_cooking_gas_hob = RiskAssessmentWithoutNumberInputs(
            activity="cooking on gas hob",
            hazard="leaving gas",
            who_it_harms="people living in the building",
            how_it_harms="explosion",
            prevention="electric hob / gas detector",
            mitigation="Use a fire extinguisher",
            prevention_prompt_expected_class="prevention",
            mitigation_prompt_expected_class="mitigation",
            risk_domain="physical risk to individuals"
        )

RA_zebra_crossing = RiskAssessmentWithoutNumberInputs(
            activity="Crossing the road",
            hazard="Careless drivers ",
            who_it_harms="Pedestrians",
            how_it_harms="Injury",
            prevention="Use zebra crossing",
            mitigation="Call emergency services",
            prevention_prompt_expected_class="prevention",
            mitigation_prompt_expected_class="mitigation",
            risk_domain="physical risk to individuals"
        )

RA_swimming_riptides = RiskAssessmentWithoutNumberInputs(
            activity="Swimming",
            hazard="Getting caught in riptides",
            who_it_harms="Potentially any swimmers in the sea ",
            how_it_harms="People can get caught in riptides and dragged out to see putting them at a very high risk of drowing",
            prevention="Only swim within marked areas that lifeguards can spot you",
            mitigation="Swim wearing a bright coloured swim cap",
            prevention_prompt_expected_class='both',
            mitigation_prompt_expected_class='mitigation',
            risk_domain="physical risk to individuals"
        )

RA_careless_drivers = RiskAssessmentWithoutNumberInputs(
            activity="Cycling",
            hazard="Careless and dangerous drivers generally ",
            who_it_harms="The cyclists",
            how_it_harms="By colliding with cyclists",
            prevention="Ensure you are visible and obeying rules of the road.",
            mitigation="Wear a helmet",
            prevention_prompt_expected_class='prevention',
            mitigation_prompt_expected_class='mitigation',
            risk_domain="physical risk to individuals"
        )

RA_cycling_safer_routes = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Take safer routes",
    mitigation = "Wear elbow padding and a helmet",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)

RA_cycling_safer_routes__neither = RiskAssessmentWithoutNumberInputs(
    activity = "Riding a Bike",
    hazard = "Getting hit",
    how_it_harms = "Could injure",
    who_it_harms = "The cyclist",
    prevention = "Cycle along busy roads",
    mitigation = "Call an ambulance",
    prevention_prompt_expected_class = "neither",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)

RA_golf_swing = RiskAssessmentWithoutNumberInputs(
    activity = "Playing Golf",
    hazard = "Swinging golf club",
    how_it_harms = "Impact injury",
    who_it_harms = "Golfer's caddy",
    prevention = "Only play shot when caddy is at a safe distance",
    mitigation = "Apply first aid",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
)

thermo_lab_hot_equipment = RiskAssessmentWithoutNumberInputs(
    activity = "thermo lab",
    hazard = "hot equipment",
    who_it_harms = "students",
    how_it_harms = "skin burn",
    prevention = "avoid touching the hot equipment",
    mitigation = "wear a lab coat",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

crossing_road_getting_hit_green_lights = RiskAssessmentWithoutNumberInputs(
    activity = "Crossing road",
    hazard = "getting hit",
    who_it_harms = "pedestrian",
    how_it_harms = "fatal crash",
    prevention = "stop lights",
    mitigation = "cross when light is green only",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
    )

crossing_road_getting_hit_call_ambulance = RiskAssessmentWithoutNumberInputs(
    activity = "Crossing road",
    hazard = "getting hit",
    who_it_harms = "pedestrian",
    how_it_harms = "fatal crash",
    prevention = "stop lights",
    mitigation = "call ambulance",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

lab_experiment_spilled_chemicals_lab_techs = RiskAssessmentWithoutNumberInputs(
    activity = "Lab Experiment",
    hazard = "Spilled Chemicals",
    who_it_harms = "Students",
    how_it_harms = "Irritates Skin",
    prevention = "Only let lab techs handle dangerous chemicals",
    mitigation = "Wear gloves",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

lab_experiment_spilled_chemicals_no_dangerous_chemicals = RiskAssessmentWithoutNumberInputs(
    activity = "Lab Experiment",
    hazard = "Spilled Chemicals",
    who_it_harms = "Students",
    how_it_harms = "Irritates Skin",
    prevention = "Do not use dangerous chemicals",
    mitigation = "Wear gloves",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

heat_engine_lab_burning_yourself_dont_run = RiskAssessmentWithoutNumberInputs(
    activity = "participating in or conducting the ME2 heat engine lab",
    hazard = "burning yourself or other people (different degrees)",
    who_it_harms = "yourself or other people around you",
    how_it_harms = "the surface of the very hot pipes carrying the fluid could come into contact with your skin and burn it",
    prevention = "don't run in the lab",
    mitigation = "wear a lab coat",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

heat_engine_lab_burning_yourself_cold_water = RiskAssessmentWithoutNumberInputs(
    activity = "participating in or conducting the ME2 heat engine lab",
    hazard = "burning yourself or other people (different degrees)",
    who_it_harms = "yourself or other people around you",
    how_it_harms = "the surface of the very hot pipes carrying the fluid could come into contact with your skin and burn it",
    prevention = "be aware of your surroundings",
    mitigation = "have a cold water supply available and accessible",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

fluids_lab_water_spill_slippery = RiskAssessmentWithoutNumberInputs(
    activity = "Fluids lab experiment",
    hazard = "Water spill out and cause slippery",
    who_it_harms = "Users",
    how_it_harms = "Spilled water can make floor slippery and people may fall over",
    prevention = "Handle containers of water with care",
    mitigation = "Mop up using a cloth immediately",
    prevention_prompt_expected_class = "neither",
    mitigation_prompt_expected_class = "prevention",
    risk_domain="physical risk to individuals"
    )

heat_transfer_lab_boiling_water = RiskAssessmentWithoutNumberInputs(
    activity = "HEAT TRANSFER LAB",
    hazard = "Boiling (hot) water",
    who_it_harms = "Students",
    how_it_harms = "Burns",
    prevention = "Do not carry cups around",
    mitigation = "Cold water tap nearby",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

running_pump_water_spillage = RiskAssessmentWithoutNumberInputs(
    activity = "Running pump in fluids lab",
    hazard = "Water spilage",
    who_it_harms = "Users",
    how_it_harms = "Water coming into contact with electronics",
    prevention = "Check for leakage before running the pump",
    mitigation = "Wear a lab coat and PPE",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

fluids_lab_water_spilt_slipping = RiskAssessmentWithoutNumberInputs(
    activity = "Fluids laboratory",
    hazard = "Water being spilt on the floor",
    who_it_harms = "Students",
    how_it_harms = "Slipping on the water on the floor causing impact injuries",
    prevention = "Do not move the water tank when it is full",
    mitigation = "If someone gets injured due to slipping apply an ice pack to the injured area and seek medical advice without delay",      
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

syringe_injecting_fuel_place_syringe_in_middle_of_table = RiskAssessmentWithoutNumberInputs(
    activity = "Using syringe for injecting fuel",
    hazard = "Stabbing yourself",
    who_it_harms = "The user ",
    how_it_harms = "Sharp blade cuts skin and causes bleeding",
    prevention = "Place syringe in the middle of the table",
    mitigation = "Wear gloves",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

dunking_in_3v3_basketball_stop_dunking = RiskAssessmentWithoutNumberInputs(
    activity = "dunking in a 3v3 game of basketball",
    hazard = "falling",
    who_it_harms = "me",
    how_it_harms = "injury of impact",
    prevention = "stop dunking",
    mitigation = "wear full body armour",
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="physical risk to individuals"
    )

RA_credit_risk = RiskAssessmentWithoutNumberInputs(
    activity='Extending credit to customers',
    hazard='Default or non-payment',
    who_it_harms='Lender or creditor',
    how_it_harms='Loss of interest income',
    prevention='Conduct thorough credit checks and set appropriate credit limits',
    mitigation='Diversify credit exposure and establish collateral or guarantees',
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="financial risk"
)

RA_interest_rate_risk = RiskAssessmentWithoutNumberInputs(
    activity='Issuing or investing in fixed-rate securities',
    hazard='Changes in interest rates',
    who_it_harms='Borrower or investor',
    how_it_harms='Decreased asset value or income',
    prevention='Analyze interest rate trends and duration of securities',
    mitigation='Utilize interest rate hedging instruments',
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="financial risk"
)

RA_liquidity_risk = RiskAssessmentWithoutNumberInputs(
    activity='Holding illiquid assets',
    hazard='Inability to convert assets into cash',
    who_it_harms='Investor or institution',
    how_it_harms='Inability to meet financial obligations or fund withdrawals',
    prevention='Maintain sufficient cash reserves',
    mitigation='Establish lines of credit or',
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="financial risk"

)

RA_operational_risk = RiskAssessmentWithoutNumberInputs(
    activity='Conducting daily operations',
    hazard='System failures',
    who_it_harms='Organization or financial institution',
    how_it_harms='Financial loss',
    prevention='Implement regular audits',
    mitigation='Invest in technology infrastructure',
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "prevention",
    risk_domain="financial risk"
)

RA_market_risk = RiskAssessmentWithoutNumberInputs(
    activity='Trading securities or commodities',
    hazard='Fluctuations in market prices',
    who_it_harms='Trader or investor',
    how_it_harms='Losses due to market movements',
    prevention='Analyze market trends',
    mitigation='Implement hedging strategies',
    prevention_prompt_expected_class = "prevention",
    mitigation_prompt_expected_class = "mitigation",
    risk_domain="financial risk"
)

### ENVIRONMENTAL
RA_wildfire_early_detection = RiskAssessmentWithoutNumberInputs(
    activity="Walking in the forest",
    hazard="Wildfire",
    who_it_harms="Residents",
    how_it_harms="Wildfires can cause extensive damage to homes",
    prevention="Use fire-resistant plants",
    mitigation="Early detection systems",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_wildfire_early_detection__neither = RiskAssessmentWithoutNumberInputs(
    activity="Trip to forest",
    hazard="Wildfire",
    who_it_harms="Residents",
    how_it_harms="Wildfires can cause extensive damage to homes",
    prevention="Use highly-flammable plants",
    mitigation="Use a flame thrower to extinguish the fire",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="environmental risk"
)

RA_wildfire_fire_resistant_infrastructure = RiskAssessmentWithoutNumberInputs(
    activity="Trip to forest",
    hazard="Wildfire",
    who_it_harms="Residents living near the forest",
    how_it_harms="Wildfire spreading to nearby homes",
    prevention="",
    mitigation="Retrofit buildings with fire-resistant materials",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_wildfire_fire_resistant_infrastructure__neither = RiskAssessmentWithoutNumberInputs(
    activity="Trip to forest",
    hazard="Wildfire",
    who_it_harms="Endangered species",
    how_it_harms="Wildfires can cause extensive damage to wildlife habitats",
    prevention="",
    mitigation="Retrofit buildings with flammable materials",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="neither",
    risk_domain="environmental risk"
)

RA_wildfire_community_preparedness = RiskAssessmentWithoutNumberInputs(
    activity="Hiking trip through the woods",
    hazard="Wildfire",
    who_it_harms="Ecosystems",
    how_it_harms="Wildfires can cause extensive damage to the environment.",
    prevention="",
    mitigation="Community wildfire response plans",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_building_retrofit = RiskAssessmentWithoutNumberInputs(
    activity="Visit to a country near a fault line",
    hazard="Earthquake",
    who_it_harms="Residents",
    how_it_harms="Earthquakes can cause extensive damage to homes.",
    prevention="",
    mitigation="Retrofit buildings and infrastructure to withstand seismic activity.",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_public_education = RiskAssessmentWithoutNumberInputs(
    activity="Visiting a country prone to earthquakes",
    hazard="Earthquake",
    who_it_harms="Drivers",
    how_it_harms="Earthquakes can damage roads.",
    prevention="",
    mitigation="Educate the public about earthquake preparedness and response.",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_earthquake_early_warning_systems = RiskAssessmentWithoutNumberInputs(
    activity="Visiting a country near the ring of fire",
    hazard="Earthquake",
    who_it_harms="Residents in the country",
    how_it_harms="Potential loss of life",
    prevention="",
    mitigation="Invest in early warning systems to detect seismic activity",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_early_warning_systems = RiskAssessmentWithoutNumberInputs(
    activity="Visiting a country near the ring of fire",
    hazard="Volcanic Eruption",
    who_it_harms="Residents in the country",
    how_it_harms="Volcanic eruptions can cause loss of life",
    prevention="",
    mitigation="Invest in early warning systems to detect volcanic activity",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_causing_ash_cloud = RiskAssessmentWithoutNumberInputs(
    activity="Volcano visit",
    hazard="Volcanic Eruption",
    who_it_harms="Airline passengers",
    how_it_harms="Flight delays and cancellations due to ash clouds from volcanic eruptions",
    prevention="",
    mitigation="Use volcanic ash data to assist in flight diversions",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_causing_ash_cloud__neither = RiskAssessmentWithoutNumberInputs(
    activity="Volcano visit",
    hazard="Volcanic Eruption",
    who_it_harms="Airline passengers",
    how_it_harms="Flight delays and cancellations due to ash clouds from volcanic eruptions",
    prevention="",
    mitigation="Use seismic activity data to assist in flight diversions",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="neither",
    risk_domain="environmental risk"
)

RA_volcano_zoning = RiskAssessmentWithoutNumberInputs(
    activity="Living near an active volcanoes",
    hazard="Volcanic Eruption",
    who_it_harms="Residents in the country",
    how_it_harms="Volcanic eruptions can cause loss of life",
    prevention="",
    mitigation="Zoning regulations to restrict development in high-risk areas.",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_zoning__neither = RiskAssessmentWithoutNumberInputs(
    activity="Living near an active volcanoes",
    hazard="Volcanic Eruption",
    who_it_harms="Residents in the country",
    how_it_harms="Volcanic eruptions can cause loss of life",
    prevention="",
    mitigation="Allow housing development near active volcanoes.",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="neither",
    risk_domain="environmental risk"
)

RA_volcano_emergency_response = RiskAssessmentWithoutNumberInputs(
    activity="Living in a country with active volcanoes",
    hazard="Volcanic Eruption",
    who_it_harms="Ecosystems",
    how_it_harms="Volcanic eruptions can cause extensive damage to the environment.",
    prevention="",
    mitigation="Develop emergency response plans",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_volcano_post_disaster_recovery = RiskAssessmentWithoutNumberInputs(
    activity="Starting a business in a country prone to volcanic eruptions",
    hazard="Volcanic Eruption",
    who_it_harms="Businesses in the country",
    how_it_harms="Disruption to supply chains leading to reduced economic activity",
    prevention="",
    mitigation="Support affected communities",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="environmental risk"
)

RA_ransomware_NHS_isolation = RiskAssessmentWithoutNumberInputs(
    activity="Delivering medical care",
    hazard="Ransomware attack",
    who_it_harms="Patients and medical staff",
    how_it_harms="Interference with healthcare operations",
    prevention="Maintain up-to-date software patches.",
    mitigation="Isolate infected system from the rest of the network",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_isolation__neither = RiskAssessmentWithoutNumberInputs(
    activity="Delivering medical care",
    hazard="Ransomware attack",
    who_it_harms="Patients and medical staff",
    how_it_harms="Interference with healthcare operations",
    prevention="Update software patches infrequently",
    mitigation="Connect the infected system to the rest of the network",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_MFA = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware attack",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Potential data loss",
    prevention="Multi-factor authentication",
    mitigation="Use decryption tools for the specific ransomware variant",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_MFA__neither = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware attack",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Potential data loss",
    prevention="Avoid using multi-factor authentication",
    mitigation="Use manual handling tools (e.g. spanner) for the specific ransomware variant", # should be decryption
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_ransomware_NHS_data_backup = RiskAssessmentWithoutNumberInputs(
    activity="Providing healthcare services",
    hazard="Ransomware",
    who_it_harms="Patients and healthcare providers",
    how_it_harms="Disruption of healthcare services",
    prevention="Train employees on how to recognize phishing emails",
    mitigation="Implement a robust data backup strategy",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_bank_cybersecurity_attack = RiskAssessmentWithoutNumberInputs(
    activity="Providing banking services",
    hazard="Phishing Attack",
    who_it_harms="Customers",
    how_it_harms="Unauthorized access to sensitive financial information",
    prevention="Train customers and employees on how to recognize phishing emails",
    mitigation="Implement email filtering solutions to detect and block phishing attempts",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="prevention",
    risk_domain="cybersecurity risk"
)

RA_transport_cyber_attack_specific = RiskAssessmentWithoutNumberInputs(
    activity="Managing transportation systems",
    hazard="Ransomware Attack on Traffic Control Systems",
    who_it_harms="Passengers",
    how_it_harms="Disruption of traffic flow",
    prevention="Regularly update and patch traffic control system software",
    mitigation="Implement robust data backup strategies",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_telecoms_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating telecommunications infrastructure",
    hazard="Cyber Attack Targeting Major UK Telecoms Network Provider",
    who_it_harms="Customers of the telecommunications service",
    how_it_harms="Potential disruption of internet and voice services for millions",
    prevention="Perform routine security evaluations.",
    mitigation="Formulate and validate incident response strategies.",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk",
)

RA_civil_nuclear_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating civil nuclear generating sites",
    hazard="Cyber Attack on Civil Nuclear Generating Site",
    who_it_harms="Energy consumers",
    how_it_harms="Temporary loss of power supply",
    prevention="Foster sector-wide collaboration against cyber-threats",
    mitigation="Develop incident response plans",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_civil_nuclear_cyber_attack__neither = RiskAssessmentWithoutNumberInputs(
    activity="Operating civil nuclear generating sites",
    hazard="Cyber Attack on Civil Nuclear Generating Site",
    who_it_harms="Energy consumers",
    how_it_harms="Temporary loss of power supply",
    prevention="Avoid sector-wide collaboration against cyber-threats",
    mitigation="Destroy incident response plans",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_electricity_infrastructure_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating the National Electicity Transmission System (NETS)",
    hazard="Cyber Attack on NETS",
    who_it_harms="Energy consumers",
    how_it_harms="Instantaneous loss of mains electricity supply",
    prevention="Empower employees to recognize and respond effectively to suspicious activities.",
    mitigation="Divide the NETS infrastructure into distinct segments", # to limit the spread of a cybersecurity attack
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_electricity_infrastructure_cyber_attack__neither = RiskAssessmentWithoutNumberInputs(
    activity="Operating the National Electicity Transmission System (NETS)",
    hazard="Cyber Attack on NETS",
    who_it_harms="Energy consumers",
    how_it_harms="Instantaneous loss of mains electricity supply",
    prevention="Teach employees how to perform a cyber attack",
    mitigation="Keep the NETS infrastructure as a single segment",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_gas_infrastructure_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating gas transmission and distribution networks",
    hazard="Encrypting of data upon which critical Gas Infrastructure systems depend",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of gas supply",
    prevention="Implement multi-factor authentication", # and access controls to protect critical systems and data
    mitigation="Develop and test incident response plans", #  to enable rapid detection, containment, and recovery from cyber attacks
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_gas_infrastructure_cyber_attack__neither = RiskAssessmentWithoutNumberInputs(
    activity="Operating gas transmission and distribution networks",
    hazard="Encrypting of data upon which critical Gas Infrastructure systems depend",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of gas supply",
    prevention="Avoid use of multi-factor authentication", # and access controls to protect critical systems and data
    mitigation="Destroy incident response plans", #  to enable rapid detection, containment, and recovery from cyber attacks
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_fuel_supply_cyber_attack = RiskAssessmentWithoutNumberInputs(
    activity="Operating fuel supply infrastructure",
    hazard="Cyber Attack on system critical to UK fuel distribution and supply",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of fuel supply",
    prevention="Conduct penetration tests to identify and address vulnerabilities", #  in fuel supply infrastructure
    mitigation="Hire cybersecurity experts to manage emergency responses", # to cyber attacks
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="cybersecurity risk"
)

RA_fuel_supply_cyber_attack__neither = RiskAssessmentWithoutNumberInputs(
    activity="Operating fuel supply infrastructure",
    hazard="Cyber Attack on system critical to UK fuel distribution and supply",
    who_it_harms="Energy consumers",
    how_it_harms="Disruption of fuel supply",
    prevention="Disinfect the computers using disinfectant", #  in fuel supply infrastructure
    mitigation="Hire earthquake response experts to manage emergency responses", # to cyber attacks
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="cybersecurity risk"
)

RA_explosive_devices_sniffer_dogs = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings or events",
    hazard="Explosive terrorist attack",
    who_it_harms="Event attendees",
    how_it_harms="Explosion leads to loss of life",
    prevention="Enhancing explosive detection capabilities", # e.g. with sniffer dogs
    mitigation="Providing victim support structures",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_explosive_devices_security = RiskAssessmentWithoutNumberInputs(
    activity="Organizing public gatherings or functions",
    hazard="Terrorist attack involving explosives",
    who_it_harms="Bystanders",
    how_it_harms="Potential for numerous fatalities and injuries",
    prevention="Conducting bag checks", # (e.g., bag screenings, surveillance)
    mitigation="Utilizing Forensic Explosives Laboratory for investigation and legal proceedings",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_explosive_devices_security__neither = RiskAssessmentWithoutNumberInputs(
    activity="Organizing public gatherings or functions",
    hazard="Terrorist attack involving explosives",
    who_it_harms="Bystanders",
    how_it_harms="Potential for numerous fatalities and injuries",
    prevention="Relaxing security during public events", # (e.g., bag screenings, surveillance)
    mitigation="Utilizing a cybersecurity response team for investigation",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="terrorism risk"
)


RA_terrorism_aviation_background_checks = RiskAssessmentWithoutNumberInputs(
    activity="Air travel operations",
    hazard="Terrorist attack targeting aircraft",
    who_it_harms="Passengers",
    how_it_harms="Loss of life of all onboard plane",
    prevention="Conducting thorough background checks on airport staff.",
    mitigation="Providing psychological support for affected individuals",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_terrorism_aviation_background_checks__neither = RiskAssessmentWithoutNumberInputs(
    activity="Air travel operations",
    hazard="Terrorist attack targeting aircraft",
    who_it_harms="Passengers",
    how_it_harms="Significant loss of life",
    prevention="Neglecting thorough background checks on airport staff",
    mitigation="Throwing the injured personnel into the sea",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="terrorism risk"
)

RA_terrorism_aviation_improving_standards = RiskAssessmentWithoutNumberInputs(
    activity="Air travel",
    hazard="Terrorist attack aimed at aircraft",
    who_it_harms="Flight crew members",
    how_it_harms="Crash of aircraft causing fatalities",
    prevention="Improve global aviation security standards",
    mitigation="Deploy search and rescue teams",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_hostage_negotiation_teams = RiskAssessmentWithoutNumberInputs(
    activity="Public gatherings",
    hazard="Hostage taking",
    who_it_harms="Hostages",
    how_it_harms="Risk of losing money to ransom",
    prevention="Implementing security measures",
    mitigation="Utilizing hostage negotiation teams",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_hostage_psychological_support = RiskAssessmentWithoutNumberInputs(
    activity="Organizing high-profile events",
    hazard="Hostage taking",
    who_it_harms="Hostages",
    how_it_harms="Infliction of psychological trauma",
    prevention="Enhancing intelligence gathering capabilities",
    mitigation="Providing psychological support",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_high_profile_assassination_protection = RiskAssessmentWithoutNumberInputs(
    activity="Public appearances or events involving high-profile figures",
    hazard="Assassination of a high-profile public figure",
    who_it_harms="High-profile public figures",
    how_it_harms="Loss of life of high profile figure",
    prevention="Providing close protection for high-profile figures",
    mitigation="Apprehending perpetrators to prevent further attacks",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_high_profile_assassination_protection__neither = RiskAssessmentWithoutNumberInputs(
    activity="Public appearances or events involving high-profile figures",
    hazard="Assassination of a high-profile public figure",
    who_it_harms="High-profile public figures",
    how_it_harms="Loss of life",
    prevention="Shoot the high-profile figure",
    mitigation="Releasing perpetrators",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="terrorism risk"
)

RA_high_profile_assassination_security_measures = RiskAssessmentWithoutNumberInputs(
    activity="Public engagements or events featuring prominent figures",
    hazard="Assassination targeting a prominent public figure",
    who_it_harms="Prominent public figures",
    how_it_harms="Fatality of high profile figure",
    prevention="Implementing robust security measures for public appearances",
    mitigation="Managing public communications to prevent escalation of tensions",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_CBRN_attack_securing_borders = RiskAssessmentWithoutNumberInputs(
    activity="Public safety and national security",
    hazard="CBRN (Chemical, Biological, Radiological, Nuclear) attack",
    who_it_harms="General population",
    how_it_harms="Contamination of food and water supplies",
    prevention="Securing borders to limit access to hazardous materials",
    mitigation="Rapid response and decontamination procedures",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

# TODO: This is a mix between a biohazard and a terrorist attack
# This confirms that you should have multiple different prompts for different risk
# domains and that certain risks can fall into multiple different domains
RA_CBRN_attack_enhance_detection = RiskAssessmentWithoutNumberInputs(
    activity="Ensuring public safety and national security",
    hazard="CBRN (Chemical, Biological, Radiological, Nuclear) threat",
    who_it_harms="Emergency responders",
    how_it_harms="Potential for significant casualties and fatalities",
    prevention="Enhancing detection methods for CBRN materials",
    mitigation="Providing medical treatment for affected individuals",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="terrorism risk"
)

RA_CBRN_attack_enhance_detection__neither = RiskAssessmentWithoutNumberInputs(
    activity="Ensuring public safety and national security",
    hazard="CBRN (Chemical, Biological, Radiological, Nuclear) threat",
    who_it_harms="Emergency responders",
    how_it_harms="Potential for significant casualties and fatalities",
    prevention="Enhancing detection methods of phishing emails",
    mitigation="Yelling at those injured",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="terrorism risk"
)

RA_pandemic_isolate_cases = RiskAssessmentWithoutNumberInputs(
    activity="Managing emergency response",
    hazard="Pandemic",
    who_it_harms="General population",
    how_it_harms="Loss of life",
    prevention="Educating the public about disease transmission", # can help reduce the spread of pathogens
    mitigation="Rapid response to identify and isolate suspected cases",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_scalable_treatment = RiskAssessmentWithoutNumberInputs(
    activity="Managing public health",
    hazard="Pandemic outbreak",
    who_it_harms="General populace",
    how_it_harms="Fatalities",
    prevention="Addressing factors contributing to the spread of infectious diseases, such as climate change",
    mitigation="Scalable diagnostics and treatment options",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_vaccines = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Businesses",
    how_it_harms="Economic disruption",
    prevention="",
    mitigation="Rapid deployment and distribution of vaccines",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_vaccines__neither = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Businesses",
    how_it_harms="Economic disruption",
    prevention="",
    mitigation="Rapid deployment and distribution of anti-virus software",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="neither",
    risk_domain="biohazard risk"
)

RA_pandemic_resource_allocation = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Students",
    how_it_harms="Disruption of education",
    prevention="",
    mitigation="Giving parents advice on how to help children learn from home",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_resource_allocation__neither = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Students",
    how_it_harms="Disruption of education",
    prevention="",
    mitigation="Encouraging parents to clap outside every Thursday for the NHS",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="neither",
    risk_domain="biohazard risk"
)

RA_pandemic_quarantine = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Individuals susceptible to depression",
    how_it_harms="Increased mental health issues",
    prevention="",
    mitigation="Allocating resources to online provision of mental health services",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_pandemic_surge_capacity = RiskAssessmentWithoutNumberInputs(
    activity="Public health and emergency response",
    hazard="Pandemic",
    who_it_harms="Patients requiring medical care",
    how_it_harms="Overwhelmed healthcare systems leading to increased fatalities",
    prevention="",
    mitigation="Implementing surge capacity plans in hospitals",
    prevention_prompt_expected_class="",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_rapid_response = RiskAssessmentWithoutNumberInputs(
    activity="Livestock farming operations",
    hazard="An outbreak of foot and mouth disease",
    who_it_harms="Livestock",
    how_it_harms="Economic losses in agriculture sector",
    prevention="Implementing farm visitor management protocols",
    mitigation="Rapid response to detect and contain outbreaks",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_rapid_response__neither = RiskAssessmentWithoutNumberInputs(
    activity="Livestock farming operations",
    hazard="An outbreak of foot and mouth disease",
    who_it_harms="Livestock",
    how_it_harms="Economic losses in agriculture sector",
    prevention="Implementing overly relaxed visitor management protocols",
    mitigation="Increasing taxes on farmers",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_culling = RiskAssessmentWithoutNumberInputs(
    activity="Management of livestock farming",
    hazard="Incidence of foot and mouth disease outbreak",
    who_it_harms="Parts of population reliant on animal protein",
    how_it_harms="Food insecurity",
    prevention="Maintaining high standards of hygiene on the farm",
    mitigation="Conducting mass culling of infected animals",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_foot_and_mouth_disease_culling__neither = RiskAssessmentWithoutNumberInputs(
    activity="Management of livestock farming",
    hazard="Incidence of foot and mouth disease outbreak",
    who_it_harms="Parts of population reliant on animal protein",
    how_it_harms="Food insecurity",
    prevention="Maintaining low standards of hygiene on the farm",
    mitigation="Avoiding the mass culling of infected animals",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="neither",
    risk_domain="biohazard risk"
)

RA_healthcare_biohazard = RiskAssessmentWithoutNumberInputs(
    activity="Healthcare facility operations involving infectious patients",
    hazard="Potential transmission of infectious diseases",
    who_it_harms="Patients",
    how_it_harms="Infections",
    prevention="Conducting regular disinfection",
    mitigation="Implementing quarantine measures",
    prevention_prompt_expected_class="prevention",
    mitigation_prompt_expected_class="mitigation",
    risk_domain="biohazard risk"
)

RA_healthcare_biohazard__neither = RiskAssessmentWithoutNumberInputs(
    activity="Healthcare facility operations involving infectious patients",
    hazard="Potential transmission of infectious diseases",
    who_it_harms="Patients",
    how_it_harms="Infections",
    prevention="Conducting disinfection once a year",
    mitigation="Giving the infected patients peanut butter",
    prevention_prompt_expected_class="neither",
    mitigation_prompt_expected_class="",
    risk_domain="biohazard risk"
)

physical_risks_to_individuals__original_student_data = {
    'risk_assessments': [
        # 10 examples to be used for how it harms test with natural disasters
        RA_syringe_needle, 
        RA_trombone_impact, 
        RA_hearing_damage, 
        RA_ink_spill_in_eye, 
        RA_wet_hands_electric_shock, 
        RA_water_tank,
        RA_sharp_drone_propeller_blade, 
        RA_incorrect_prevention_and_mitigation,
        RA_heavy_weight_falls_on_demonstrator, 
        RA_zip_tie_hits_audience,
        RA_battery_causes_fire, 

        # Neither examples
        RA_syringe_needle__neither,
        RA_ink_spill_in_eye__neither,
        RA_wet_hands_electric_shock__neither,
        RA_water_tank__neither,
        RA_mucking_out_horse__neither,
        RA_battery_causes_fire__neither,
        
        RA_paper_plane_impact, 
        RA_pencil_lead_projectile,
        RA_climbing_gear_on_feet, 
        ],
    'risk_domain': 'Physical risks to individuals (original student data)'
}

physical_risks_to_individuals_with_unique_hazard_description_fields = {
    'risk_assessments': [
        RA_sharp_drone_propeller_blade,
        # RA_zip_tie_hits_audience,
        # RA_pencil_lead_projectile,
        # RA_heavy_weight_falls_on_demonstrator,
        # RA_syringe_needle,
        # RA_cycling,
        # RA_swimming_riptides,
        # fluids_lab_water_spill_slippery
    ],
    'risk_domain': 'Physical risks'
}

physical_risk_assessments_that_have_suitable_who_it_harms_fields_for_risk_domain_test = {
    'risk_assessments': [
        RA_golf_swing,
        # RA_ladder,
        # RA_sharp_drone_propeller_blade,
        # RA_battery_causes_fire,
        # RA_heavy_weight_falls_on_demonstrator,
        # RA_crossing_road,
        # RA_mucking_out_horse,
        # RA_bouldering,

    ],
    'risk_domain': 'Physical risks'
}

physical_risks_to_individuals__data_gathered_from_version_1_deployment = {
    'risk_assessments': [
        # RA_fire_alarm,
        # RA_mop_up_spill,
        # RA_mop_up_spill_correct_hazard_event_and_harm_caused,
        # RA_syringe_with_cover,
        # RA_hot_water_in_cups,
        # RA_bigger_beaker,
        RA_cycling_high_viz,
        # RA_mucking_out_horse,
        # RA_slitter_machine,
        # RA_campfire,
        # RA_bouldering,
        # RA_hob_burn,
        # RA_crossing_road,
        # RA_cycling,
        # RA_ladder,
        # RA_stable_ladder,
        # RA_cooking_gas_hob,
        # RA_zebra_crossing,
        # RA_swimming_riptides,
        # RA_careless_drivers,
        # RA_cycling_safer_routes,
        # RA_golf_swing,
        
        # thermo_lab_hot_equipment,
        # crossing_road_getting_hit_green_lights,
        # crossing_road_getting_hit_call_ambulance,
        # lab_experiment_spilled_chemicals_lab_techs,
        # lab_experiment_spilled_chemicals_no_dangerous_chemicals,
        # heat_engine_lab_burning_yourself_dont_run,
        # heat_engine_lab_burning_yourself_cold_water,
        # fluids_lab_water_spill_slippery,
        # heat_transfer_lab_boiling_water,
        # running_pump_water_spillage,
        # fluids_lab_water_spilt_slipping,
        # syringe_injecting_fuel_place_syringe_in_middle_of_table,
        # dunking_in_3v3_basketball_stop_dunking,
        
        # # # Neither examples
        # RA_campfire__neither,
        # RA_bouldering__neither,
        # RA_hob_burn__neither,
        # RA_cycling_high_viz__neither,
        # RA_cycling_safer_routes__neither,
    ],
    'risk_domain': 'Physical risks to individuals (data gathered from version 1 deployment)'
}

physical_risks_to_individuals = {
    'risk_assessments': physical_risks_to_individuals__original_student_data['risk_assessments'] + physical_risks_to_individuals__data_gathered_from_version_1_deployment['risk_assessments'],
    'risk_domain': 'Physical risks to individuals'
}

finance_risks = {
    'risk_assessments': [
        RA_credit_risk,
        RA_interest_rate_risk,
        RA_liquidity_risk,
        RA_operational_risk,
        RA_market_risk
    ],
    'risk_domain': 'Financial risks'
}

natural_disaster_risks = {
    'risk_assessments': [
        # MITIGATION ONLY
        RA_wildfire_fire_resistant_infrastructure,
        # RA_wildfire_community_preparedness,
        # RA_earthquake_building_retrofit,
        # RA_earthquake_public_education,
        # RA_earthquake_early_warning_systems,
        # RA_volcano_early_warning_systems,
        # RA_volcano_causing_ash_cloud,
        # RA_volcano_zoning,
        # RA_volcano_emergency_response,
        # RA_volcano_post_disaster_recovery,

        # # PREVENTION AND MITIGATION
        # RA_wildfire_early_detection,

        # # NEITHER EXAMPLES
        # RA_wildfire_early_detection__neither,
        # RA_wildfire_fire_resistant_infrastructure__neither,
        # RA_volcano_causing_ash_cloud__neither,
        # RA_volcano_zoning__neither,

    ],
    'risk_domain': 'Natural disaster risks'
}

natural_disaster_risks_with_unique_hazard_description_fields = {
    'risk_assessments': [
        RA_wildfire_fire_resistant_infrastructure,
        # RA_wildfire_community_preparedness,
        # RA_earthquake_building_retrofit,
        # RA_earthquake_public_education,
        # RA_volcano_early_warning_systems,
        # RA_volcano_causing_ash_cloud,
        # RA_volcano_post_disaster_recovery,
        # heat_engine_lab_burning_yourself_dont_run,
    ],
    'risk_domain': 'Natural disaster risks'
}

natural_disaster_risk_assessments_that_have_suitable_who_it_harms_fields_for_risk_domain_test = {
    'risk_assessments': [
        RA_wildfire_community_preparedness,
        # RA_wildfire_fire_resistant_infrastructure__neither,
        # RA_volcano_causing_ash_cloud,
        # RA_volcano_post_disaster_recovery
    ],
    'risk_domain': 'Natural disaster risks'
}

cybersecurity_risks = {
    'risk_assessments': [
        RA_ransomware_NHS_isolation,
        RA_ransomware_NHS_MFA,
        RA_ransomware_NHS_data_backup,
        RA_bank_cybersecurity_attack,
        RA_transport_cyber_attack_specific,
        RA_telecoms_cyber_attack,
        RA_civil_nuclear_cyber_attack,
        RA_electricity_infrastructure_cyber_attack,
        RA_gas_infrastructure_cyber_attack,
        RA_fuel_supply_cyber_attack,

        # NEITHER EXAMPLES
        RA_ransomware_NHS_isolation__neither,
        RA_ransomware_NHS_MFA__neither,
        RA_civil_nuclear_cyber_attack__neither,
        RA_electricity_infrastructure_cyber_attack__neither,
        RA_gas_infrastructure_cyber_attack__neither,
        RA_fuel_supply_cyber_attack__neither,
    ],
    'risk_domain': 'Cybersecurity risks'
}

cybersecurity_risks_with_unique_hazard_description_fields = {
    'risk_assessments': [
        RA_ransomware_NHS_isolation,
        # RA_ransomware_NHS_MFA,
        # RA_ransomware_NHS_data_backup,
        # RA_bank_cybersecurity_attack,
        # RA_transport_cyber_attack_specific,
        # RA_telecoms_cyber_attack,
        # RA_civil_nuclear_cyber_attack,
        # RA_electricity_infrastructure_cyber_attack,
    ],
    'risk_domain': 'Cybersecurity risks'
}

cybersecurity_risk_assessments_that_have_suitable_who_it_harms_fields_for_risk_domain_test = {
    'risk_assessments': [
        RA_telecoms_cyber_attack,
        # RA_civil_nuclear_cyber_attack
    ],
    'risk_domain': 'Cybersecurity risks'
}

terrorism_risks = {
    'risk_assessments': [
        RA_explosive_devices_sniffer_dogs,
        RA_explosive_devices_security,
        RA_terrorism_aviation_background_checks,
        RA_terrorism_aviation_improving_standards,
        RA_hostage_negotiation_teams,
        RA_hostage_psychological_support,
        RA_high_profile_assassination_protection,
        RA_high_profile_assassination_security_measures,
        RA_CBRN_attack_enhance_detection,
        RA_CBRN_attack_securing_borders,

        # NEITHER EXAMPLES
        RA_explosive_devices_security__neither,
        RA_terrorism_aviation_background_checks__neither,
        RA_high_profile_assassination_protection__neither,
        RA_CBRN_attack_enhance_detection__neither,
        
    ],
    'risk_domain': 'Terrorism risks'
}

terrorism_risks_with_unique_hazard_description_fields = {
    'risk_assessments': [
        RA_explosive_devices_sniffer_dogs,
        # RA_terrorism_aviation_background_checks,
        # RA_terrorism_aviation_improving_standards,
        # RA_hostage_negotiation_teams,
        # RA_hostage_psychological_support,
        # RA_high_profile_assassination_protection,
        # RA_high_profile_assassination_security_measures,
        # RA_CBRN_attack_securing_borders
    ],
    'risk_domain': 'Terrorism risks'
}

terrorism_risk_assessments_that_have_suitable_who_it_harms_fields_for_risk_domain_test = {
    'risk_assessments': [
        RA_hostage_negotiation_teams
    ],
    'risk_domain': 'Terrorism risks'
}

biohazard_risks = {
    'risk_assessments': [
    # MITIGATION ONLY
    RA_pandemic_resource_allocation,
    RA_pandemic_surge_capacity,
    RA_pandemic_quarantine,
    RA_pandemic_vaccines,

    # PREVENTION AND MITIGATION
    RA_pandemic_isolate_cases,
    RA_pandemic_scalable_treatment,
    RA_foot_and_mouth_disease_culling,
    RA_foot_and_mouth_disease_rapid_response,
    RA_healthcare_biohazard,

    # NEITHER EXAMPLES
    RA_pandemic_resource_allocation__neither,
    RA_pandemic_vaccines__neither,
    RA_foot_and_mouth_disease_culling__neither,
    RA_foot_and_mouth_disease_rapid_response__neither,
    RA_healthcare_biohazard__neither
    ],

    'risk_domain': 'biohazard risks'
}

biohazard_risks_with_unique_hazard_description_fields = {
    'risk_assessments': [
        RA_pandemic_surge_capacity,
        # RA_pandemic_quarantine,
        # RA_pandemic_vaccines,
        # RA_foot_and_mouth_disease_rapid_response
    ],
    'risk_domain': 'Biohazard risks'
}

biohazard_risk_assessments_that_have_suitable_who_it_harms_fields_for_risk_domain_test = {
    'risk_assessments': [
        RA_pandemic_surge_capacity,
        # RA_foot_and_mouth_disease_rapid_response,
        # RA_pandemic_quarantine
    ],
    'risk_domain': 'Biohazard risks'
}

# all_risk_assessments = []

# for risk_assessments_dict in [
#         physical_risks_to_individuals__data_gathered_from_version_1_deployment,
#         physical_risks_to_individuals__original_student_data,
#         natural_disaster_risks,
#         cybersecurity_risks,
#         terrorism_risks,
#         biohazard_risks
#     ]:

#     all_risk_assessments += risk_assessments_dict['risk_assessments']

# def create_risk_assessments_with_how_it_harms_replaced_with_activity(risk_assessments):
#     new_risk_assessments = []

#     for risk_assessment in risk_assessments:
#         risk_assessment.update_risk_assessment_so_how_it_harms_field_is_activity_field()

#         new_risk_assessments.append(risk_assessment)
    
#     return new_risk_assessments

def create_unique_set_of_control_measures(risk_assessments):
    unique_control_measures = set()

    for risk_assessment in risk_assessments:
        if risk_assessment.prevention != "":
            unique_control_measures.add(risk_assessment.prevention)
        if risk_assessment.mitigation != "":
            unique_control_measures.add(risk_assessment.mitigation)
    
    return unique_control_measures