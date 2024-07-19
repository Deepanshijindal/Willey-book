
##################################################################

class InputData:
    def __init__(self, id):
        self.id = id
        self.data = self.input_fun()

    def input_fun(self):
        input_data = {}
        if self.id == 10:
            input_data = {
                'cities': ['Bristol', 'Brighton', 'London'],
                'offices': ['A', 'B', 'C', 'D', 'E'],
                'benefits': {
                    'Bristol': {'A': 10000, 'B': 15000, 'C': 10000, 'D': 20000, 'E': 5000},
                    'Brighton': {'A': 10000, 'B': 20000, 'C': 15000, 'D': 15000, 'E': 15000},
                    'London': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
                },
                'quantities_of_communication': {
                    'A': {'A': 0.0, 'B': 0.0, 'C': 1000.0, 'D': 1500.0, 'E': 0.0},
                    'B': {'A': 0.0, 'B': 0.0, 'C': 1400.0, 'D': 1200.0, 'E': 0.0},
                    'C': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 2000.0},
                    'D': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 700.0},
                    'E': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0}
                },
                'costs_per_unit_of_communication': {
                    'Bristol': {'Bristol': 5, 'Brighton': 14, 'London': 13},
                    'Brighton': {'Bristol': 14, 'Brighton': 5, 'London': 9},
                    'London': {'Bristol': 13, 'Brighton': 9, 'London': 10}
                }
            }
        elif self.id == 11.1 or self.id == 11.2 or self.id == 11.3:
            input_data = {
                'X': [0.0, 0.5, 1.0, 1.5, 1.9, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.6, 7.0, 7.6, 8.5, 9.0, 10.0],
                'Y': [1.0, 0.9, 0.7, 1.5, 2.0, 2.4, 3.2, 2.0, 2.7, 3.5, 1.0, 4.0, 3.6, 2.7, 5.7, 4.6, 6.0, 6.8, 7.3],
            }
            # Add data for question 1
        elif self.id == 13 or self.id == 13.2:
            # Define the data
            retailers_data = {
                'M1': {'region': 1, 'oil': 9, 'delivery_points': 11, 'spirit': 34, 'growth': 'A'},
                'M2': {'region': 1, 'oil': 13, 'delivery_points': 47, 'spirit': 411, 'growth': 'A'},
                'M3': {'region': 1, 'oil': 14, 'delivery_points': 44, 'spirit': 82, 'growth': 'A'},
                'M4': {'region': 1, 'oil': 17, 'delivery_points': 25, 'spirit': 157, 'growth': 'B'},
                'M5': {'region': 1, 'oil': 18, 'delivery_points': 10, 'spirit': 5, 'growth': 'A'},
                'M6': {'region': 1, 'oil': 19, 'delivery_points': 26, 'spirit': 183, 'growth': 'A'},
                'M7': {'region': 1, 'oil': 23, 'delivery_points': 26, 'spirit': 14, 'growth': 'B'},
                'M8': {'region': 1, 'oil': 21, 'delivery_points': 54, 'spirit': 215, 'growth': 'B'},
                'M9': {'region': 2, 'oil': 9, 'delivery_points': 18, 'spirit': 102, 'growth': 'B'},
                'M10': {'region': 2, 'oil': 11, 'delivery_points': 51, 'spirit': 21, 'growth': 'A'},
                'M11': {'region': 2, 'oil': 17, 'delivery_points': 20, 'spirit': 54, 'growth': 'B'},
                'M12': {'region': 2, 'oil': 18, 'delivery_points': 105, 'spirit': 0, 'growth': 'B'},
                'M13': {'region': 2, 'oil': 18, 'delivery_points': 7, 'spirit': 6, 'growth': 'B'},
                'M14': {'region': 2, 'oil': 17, 'delivery_points': 16, 'spirit': 96, 'growth': 'B'},
                'M15': {'region': 2, 'oil': 22, 'delivery_points': 34, 'spirit': 118, 'growth': 'A'},
                'M16': {'region': 2, 'oil': 24, 'delivery_points': 100, 'spirit': 112, 'growth': 'B'},
                'M17': {'region': 2, 'oil': 36, 'delivery_points': 50, 'spirit': 535, 'growth': 'B'},
                'M18': {'region': 2, 'oil': 43, 'delivery_points': 21, 'spirit': 8, 'growth': 'B'},
                'M19': {'region': 3, 'oil': 6, 'delivery_points': 11, 'spirit': 53, 'growth': 'B'},
                'M20': {'region': 3, 'oil': 15, 'delivery_points': 19, 'spirit': 28, 'growth': 'A'},
                'M21': {'region': 3, 'oil': 15, 'delivery_points': 14, 'spirit': 69, 'growth': 'B'},
                'M22': {'region': 3, 'oil': 25, 'delivery_points': 10, 'spirit': 65, 'growth': 'B'},
                'M23': {'region': 3, 'oil': 39, 'delivery_points': 11, 'spirit': 27, 'growth': 'B'},
            }

            # Helper dictionaries to store retailers by region and by growth category
            retailers_by_region = {1: [], 2: [], 3: []}
            retailers_by_growth = {'A': [], 'B': []}

            # Populate the helper dictionaries
            for retailer, data in retailers_data.items():
                retailers_by_region[data['region']].append(retailer)
                retailers_by_growth[data['growth']].append(retailer)
            # Initialize sums
            total_delivery_point = 0
            total_spirit = 0

            # Calculate the sums
            for retailer, data in retailers_data.items():
                total_delivery_point += data['delivery_points']
                total_spirit += data['spirit']

            total_oil_region_1 = sum(retailer['oil'] for retailer in retailers_data.values() if retailer['region'] == 1)
            total_oil_region_2 = sum(retailer['oil'] for retailer in retailers_data.values() if retailer['region'] == 2)
            total_oil_region_3 = sum(retailer['oil'] for retailer in retailers_data.values() if retailer['region'] == 3)

            # Combine everything into a single nested dictionary
            input_data = {
                'retailers_data': retailers_data,
                'retailers_by_region': retailers_by_region,
                'retailers_by_growth': retailers_by_growth,
                'retailers': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23' ],
                'total_delivery_points' : total_delivery_point,
                'total_spirit' : total_spirit,
                'total_oil_region_1' : total_oil_region_1,
                'total_oil_region_2' : total_oil_region_2,
                'total_oil_region_3' : total_oil_region_3
            }


        elif self.id == 14:
            input_data = {
                "plot_size": (200, 200),  # Dimensions of the square plot in feet

                "block_size": {
                    "horizontal": 50,  # Horizontal dimension of each block in feet
                    "vertical": 25      # Vertical dimension of each block in feet
                },

                "angle_of_slip": 45,  # Maximum angle of slip in degrees

                "ore_values": {
                    1: [ 1.5, 1.5, 1.5, 0.75, 1.5, 2.0, 1.5, 0.75, 1.0, 1.0, 0.75, 0.5, 0.75, 0.75, 0.5, 0.25],
                    2: [4.0, 4.0, 2.0, 3.0, 3.0, 1.0, 2.0, 2.0, 0.5],
                    3: [12.0, 6.0, 5.0, 4.0],
                    4: [6.0]
                },

                "extraction_costs": {
                    1: 3000,  # Cost of extraction at level 1
                    2: 6000,  # Cost of extraction at level 2
                    3: 8000,  # Cost of extraction at level 3
                    4: 10000  # Cost of extraction at level 4
                },

                "revenue_per_100_value_block": 200000  # Revenue obtained from a 100% value block
            }




        elif self.id == 15:

            problems = {
            0: {
                "Minimum level": 850,
                "Maximum level": 2000,
                "Cost per hour at minimum": 1000,
                "Cost per hour per megawatt above minimum": 2,
                "Cost": 2000
            },
            1: {
                "Minimum level": 1250,
                "Maximum level": 1750,
                "Cost per hour at minimum": 2600,
                "Cost per hour per megawatt above minimum": 1.30,
                "Cost": 1000
            },
            2: {
                "Minimum level": 1500,
                "Maximum level": 4000,
                "Cost per hour at minimum": 3000,
                "Cost per hour per megawatt above minimum": 3,
                "Cost": 500
            }
        }

            input_data = {
                'periods' : range(5),
                'durations' : [6,3,6,3,6],
                'demands_by_period': [1500,30000,25000,40000,27000],
                'property' : problems,
                'types' : range(2)
            }
        # Add more elif statements for other question IDs if needed

        elif self.id == 19:
            # Define input data
            factories = ['Liverpool', 'Brighton']
            depots = ['Newcastle', 'Birmingham', 'London', 'Exeter']
            customers = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

            # Costs from factories to depots
            costs_fd = {
                'Liverpool': {'Newcastle': 0.5, 'Birmingham': 0.5, 'London': 1.0, 'Exeter': 0.2},
                'Brighton': {'Newcastle': None, 'Birmingham': 0.3, 'London': 0.5, 'Exeter': 0.2}
            }

            # Costs from factories to customers
            costs_fc = {
                'Liverpool': {'C1': 1.0, 'C2': None, 'C3': 1.5, 'C4': 2.0, 'C5': None, 'C6': 1.0},
                'Brighton': {'C1': 2.0, 'C2': None, 'C3': None, 'C4': None, 'C5': None, 'C6': None}
            }

            # Costs from depots to customers
            costs_dc = {
                'Newcastle': {'C1': None, 'C2': 1.5, 'C3': 0.5, 'C4': 1.5, 'C5': None, 'C6': 1.0},
                'Birmingham': {'C1': 1.0, 'C2': 0.5, 'C3': 0.5, 'C4': 1.0, 'C5': 0.5, 'C6': None},
                'London': {'C1': None, 'C2': 1.5, 'C3': 2.0, 'C4': None, 'C5': 0.5, 'C6': 1.5},
                'Exeter': {'C1': None, 'C2': None, 'C3': 0.2, 'C4': 1.5, 'C5': 0.5, 'C6': 1.5}
            }

            # Preferred suppliers
            preferred_suppliers = {
                'C1': 'Liverpool',
                'C2': 'Newcastle',
                'C3': None,
                'C4': None,
                'C5': 'Birmingham',
                'C6': ['Exeter', 'London']  # Multiple preferences
            }

            # Factory capacities
            factory_capacity = {
                'Liverpool': 150000,
                'Brighton': 200000
            }

            # Depot capacities
            depot_capacity = {
                'Newcastle': 70000,
                'Birmingham': 50000,
                'London': 100000,
                'Exeter': 40000
            }

            # Customer demands
            customer_demand = {
                'C1': 50000,
                'C2': 10000,
                'C3': 40000,
                'C4': 35000,
                'C5': 60000,
                'C6': 20000
            }

            input_data = { 
                'factories': factories,
                'depots' : depots,
                'customers' : customers,
                'costs_fd' : costs_fd,
                'costs_fc' : costs_fc,
                'costs_dc' : costs_dc,
                'preferred_suppliers': preferred_suppliers,
                'factory_capacity' : factory_capacity,
                'depot_capacity' : depot_capacity,
                'customer_demand' : customer_demand
            }
        return input_data
