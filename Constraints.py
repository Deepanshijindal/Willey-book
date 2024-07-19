

#################################################################
class Constraints:
    def __init__(self, id):
        self.id = id

    def add_constraints(self, model, data, vars):
        if self.id == 10:
            self._add_constraints_question_10(model,data,vars)
        elif self.id == 11.1:
            self._add_constraints_question_11_1(model,data,vars) 
        elif self.id == 11.2:
            self._add_constraints_question_11_2(model,data,vars) 
        elif self.id == 11.3:
            self._add_constraints_question_11_3(model,data,vars)
        elif self.id == 13:
            self._add_constraints_question_13(model,data,vars)
        elif self.id == 13.2:
            self._add_constraints_question_13_2(model,data,vars)  
        elif self.id == 15:
            self._add_constraints_question_15(model,data,vars)  
        elif self.id == 19:
            self._add_constraints_question_19(model,data,vars)                


        # Add more elif statements for other questions if needed

    def _add_constraints_question_10(self,model,data,vars):
        for i in range(len(data['offices'])):
            for k in range(len(data['offices'])):
                for j in range(len(data['cities'])):
                    for l in range(len(data['cities'])):
                        if k > i:
                            model.addConstr(
                                vars['gamma'][data['offices'][i], data['cities'][j], data['offices'][k], data['cities'][l]] - vars['office_city'][data['offices'][i], data['cities'][j]] <= 0,
                                name=f"c1_{data['offices'][i]}_{data['cities'][j]}_{data['offices'][k]}_{data['cities'][l]}"
                            )
                            model.addConstr(
                                vars['gamma'][data['offices'][i], data['cities'][j], data['offices'][k], data['cities'][l]] - vars['office_city'][data['offices'][k], data['cities'][l]] <= 0,
                                name=f"c2_{data['offices'][i]}_{data['cities'][j]}_{data['offices'][k]}_{data['cities'][l]}"
                            )
                            model.addConstr(
                                vars['office_city'][data['offices'][i], data['cities'][j]] + vars['office_city'][data['offices'][k], data['cities'][l]] - vars['gamma'][data['offices'][i], data['cities'][j], data['offices'][k], data['cities'][l]] <= 1,
                                name=f"c3_{data['offices'][i]}_{data['cities'][j]}_{data['offices'][k]}_{data['cities'][l]}"
                            )
        for office in data['offices']:
            model.addConstr(sum(vars['office_city'][office, city] for city in data['cities']) == 1, f"OneCity_{office}")
        for city in data['cities']:
            model.addConstr(sum(vars['office_city'][office, city] for office in data['offices']) <= 3, f"Maxoffices_{city}")
    


    def _add_constraints_question_11_1(self,model,data,vars):
        
        for i in range(len(data['Y'])):
            model.addConstr(vars['abs_dev'][i] >= data['Y'][i] - vars['a'] * data['X'][i] - vars['b'],  f"abs_dev_pos_{i}")
            model.addConstr(vars['abs_dev'][i] >= -data['Y'][i]+ vars['a'] * data['X'][i] + vars['b'], f"abs_dev_neg_{i}")


    def _add_constraints_question_11_2(self,model,data,vars):  
        for i in range(19):    
            model.addConstr(-data['Y'][i]+ vars['a'] * data['X'][i] + vars['b'] <= vars['max_dev'], f"max_dev_neg_{i}")
            model.addConstr(data['Y'][i] - vars['a'] * data['X'][i] - vars['b'] <= vars['max_dev'] ,  f"max_dev_pos_{i}")

    def _add_constraints_question_11_3(self,model,data,vars): 
        for i in range(19):    
            model.addConstr(-data['Y'][i]+ vars['c'] * (data['X'][i])**2 + vars['b']*data['X'][i] + vars['a']  <= vars['max_dev'], f"max_dev_neg_{i}")
            model.addConstr(data['Y'][i] - vars['c'] * (data['X'][i])**2 - vars['b']*data['X'][i] - vars['a'] <= vars['max_dev'] ,  f"max_dev_pos_{i}")
    
    def _add_constraints_question_13(self, model, data, vars):
        total_DP = data['total_delivery_points']
        retailers_data = data['retailers_data']
        binary_assign = vars['retailer_assign']
        retailers_list = data['retailers']
        Total_spirit = data['total_spirit']
        retailers_in_region_1 = data['retailers_by_region'][1]
        retailers_in_region_2 = data['retailers_by_region'][2]
        retailers_in_region_3 = data['retailers_by_region'][3]
        retailers_in_group_A = data['retailers_by_growth']['A']
        retailers_in_group_B = data['retailers_by_growth']['B']
        Total_oil_in_region_1 = data['total_oil_region_1']
        Total_oil_in_region_2 = data['total_oil_region_2']
        Total_oil_in_region_3 = data['total_oil_region_3']

        #Delivery points constraints
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list) <= 0.45*total_DP)
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list) >= 0.35*total_DP)
        model.addConstr((sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list)/total_DP - 0.40) <= vars['abs_delivery_points'])
        model.addConstr((-sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list)/total_DP + 0.40) <= vars['abs_delivery_points'])

        #Spirit constraints
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list) <= 0.45*Total_spirit)
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list) >= 0.35*Total_spirit)
        model.addConstr((sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list)/Total_spirit - 0.40) <= vars['abs_spirit'])
        model.addConstr((-sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list)/Total_spirit + 0.40) <= vars['abs_spirit'])

        # Oil in region1 , 2 and 3 constraints
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1) <= 0.45*Total_oil_in_region_1)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1) >= 0.35*Total_oil_in_region_1)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1)/Total_oil_in_region_1 - 0.40) <= vars['abs_oil_R1'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1)/Total_oil_in_region_1 + 0.40) <= vars['abs_oil_R1'])     

        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2) <= 0.45*Total_oil_in_region_2)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2) >= 0.35*Total_oil_in_region_2)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2)/Total_oil_in_region_2 - 0.40) <= vars['abs_oil_R2'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2)/Total_oil_in_region_2 + 0.40) <= vars['abs_oil_R2'])   


        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3) <= 0.45*Total_oil_in_region_3)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3) >= 0.35*Total_oil_in_region_3)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3)/Total_oil_in_region_3 - 0.40) <= vars['abs_oil_R3'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3)/Total_oil_in_region_3 + 0.40) <= vars['abs_oil_R3'])   

        #Constraints on group A retailers
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_A) <= 0.45*len(retailers_in_group_A))
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_A) >= 0.35*len(retailers_in_group_A))
        model.addConstr((sum(binary_assign[i]for i in retailers_in_group_A)/len(retailers_in_group_A) - 0.40) <= vars['abs_group_A'])
        model.addConstr((-sum(binary_assign[i]for i in retailers_in_group_A)/len(retailers_in_group_A) + 0.40) <= vars['abs_group_A'])
        
        #Constraints on group B retailers
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_B) <= 0.45*len(retailers_in_group_B))
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_B) >= 0.35*len(retailers_in_group_B))     
        model.addConstr((sum(binary_assign[i]for i in retailers_in_group_B)/len(retailers_in_group_B) - 0.40) <= vars['abs_group_B'])
        model.addConstr((-sum(binary_assign[i]for i in retailers_in_group_B)/len(retailers_in_group_B) + 0.40) <= vars['abs_group_B'])           

    
    def _add_constraints_question_13_2(self, model, data, vars):
        total_DP = data['total_delivery_points']
        retailers_data = data['retailers_data']
        binary_assign = vars['retailer_assign']
        retailers_list = data['retailers']
        Total_spirit = data['total_spirit']
        retailers_in_region_1 = data['retailers_by_region'][1]
        retailers_in_region_2 = data['retailers_by_region'][2]
        retailers_in_region_3 = data['retailers_by_region'][3]
        retailers_in_group_A = data['retailers_by_growth']['A']
        retailers_in_group_B = data['retailers_by_growth']['B']
        Total_oil_in_region_1 = data['total_oil_region_1']
        Total_oil_in_region_2 = data['total_oil_region_2']
        Total_oil_in_region_3 = data['total_oil_region_3']

        #Delivery points constraints
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list) <= 0.45*total_DP)
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list) >= 0.35*total_DP)
        model.addConstr((sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list)/total_DP - 0.40) <= vars['abs_delivery_points'])
        model.addConstr((-sum(binary_assign[i]* retailers_data[i]['delivery_points']for i in retailers_list)/total_DP + 0.40) <= vars['abs_delivery_points'])

        #Spirit constraints
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list) <= 0.45*Total_spirit)
        model.addConstr(sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list) >= 0.35*Total_spirit)
        model.addConstr((sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list)/Total_spirit - 0.40) <= vars['abs_spirit'])
        model.addConstr((-sum(binary_assign[i]* retailers_data[i]['spirit']for i in retailers_list)/Total_spirit + 0.40) <= vars['abs_spirit'])

        # Oil in region1 , 2 and 3 constraints
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1) <= 0.45*Total_oil_in_region_1)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1) >= 0.35*Total_oil_in_region_1)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1)/Total_oil_in_region_1 - 0.40) <= vars['abs_oil_R1'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_1)/Total_oil_in_region_1 + 0.40) <= vars['abs_oil_R1'])     

        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2) <= 0.45*Total_oil_in_region_2)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2) >= 0.35*Total_oil_in_region_2)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2)/Total_oil_in_region_2 - 0.40) <= vars['abs_oil_R2'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_2)/Total_oil_in_region_2 + 0.40) <= vars['abs_oil_R2'])   


        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3) <= 0.45*Total_oil_in_region_3)
        model.addConstr(sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3) >= 0.35*Total_oil_in_region_3)
        model.addConstr((sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3)/Total_oil_in_region_3 - 0.40) <= vars['abs_oil_R3'])
        model.addConstr((-sum(retailers_data[i]['oil']* binary_assign[i]for i in retailers_in_region_3)/Total_oil_in_region_3 + 0.40) <= vars['abs_oil_R3'])   

        #Constraints on group A retailers
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_A) <= 0.45*len(retailers_in_group_A))
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_A) >= 0.35*len(retailers_in_group_A))
        model.addConstr((sum(binary_assign[i]for i in retailers_in_group_A)/len(retailers_in_group_A) - 0.40) <= vars['abs_group_A'])
        model.addConstr((-sum(binary_assign[i]for i in retailers_in_group_A)/len(retailers_in_group_A) + 0.40) <= vars['abs_group_A'])
        
        #Constraints on group B retailers
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_B) <= 0.45*len(retailers_in_group_B))
        model.addConstr(sum(binary_assign[i]for i in retailers_in_group_B) >= 0.35*len(retailers_in_group_B))     
        model.addConstr((sum(binary_assign[i]for i in retailers_in_group_B)/len(retailers_in_group_B) - 0.40) <= vars['abs_group_B'])
        model.addConstr((-sum(binary_assign[i]for i in retailers_in_group_B)/len(retailers_in_group_B) + 0.40) <= vars['abs_group_B'])                   

        # maximum deviation constraint
        model.addConstr(vars['max_deviation']>= vars['abs_delivery_points'])
        model.addConstr(vars['max_deviation']>= vars['abs_spirit'])     
        model.addConstr(vars['max_deviation']>=vars['abs_group_A'])
        model.addConstr(vars['max_deviation']>=vars['abs_group_B'])   
        model.addConstr(vars['max_deviation']>=vars['abs_oil_R1'])   
        model.addConstr(vars['max_deviation']>=vars['abs_oil_R2'])
        model.addConstr(vars['max_deviation']>=vars['abs_oil_R3'])

    # def _add_constraints_question_14(self,model,data,vars): 
    #     for i in range(1,31):    
    #         if i == 0:
    #             vars['select_box'][i] <= vars['select_box'][i+1]
    #             vars['select_box'][i] <= vars['select_box'][i+2]
    #             vars['select_box'][i] <= vars['select_box'][i+3]
    #             vars['select_box'][i] <= vars['select_box'][i+4]

    #         if i !=0:
                


    #         model.addConstr()
    #         model.addConstr(data['Y'][i] - vars['c'] * (data['X'][i])**2 - vars['b']*data['X'][i] - vars['a'] <= vars['max_dev'] ,  f"max_dev_pos_{i}")
    def _add_constraints_question_15(self,model,data,vars): 
        # constraints which represnts the minimum and maximum values limits on output from each type 
        for period in range(5):
            for i in range(2):
                model.addConstr(vars['output_period_type'][period, i] >= vars[i+1][period]*data['property'][i]['Minimum level']) # here 0,1,2 represents type1, type2, type3
                model.addConstr(vars['output_period_type'][period, i] <= vars[i+1][period]*data['property'][i]['Maximum level'])

            # constraint for demand fullfillment by period
            model.addConstr(sum(vars['output_period_type'][period,i] for i in data['types']) >= data['demands_by_period'][period])
            
            #started generators should  be sufficient to generate power if around 15% more in every period demand
            model.addConstr((vars['start_1'][period] * data['property'][0]['Maximum level'] +
                              vars['start_2'][period]*data['property'][1]['Maximum level'] + 
                              vars['start_3'][period]*data['property'][2]['Maximum level']) >= 1.15*data['demands_by_period'][period])
            
            # The number of generarors started in period j should be equal to the change in number of working geneartors between period j and period j-1
            # that means s_i,j = n_i,j - n_i,j-1
            if period == 0:
                prev_period = len(data['periods']) - 1
            else:
                prev_period = period - 1
            
            model.addConstr(vars['start_1'][period] >= vars[1][period] - vars[1][prev_period])
            model.addConstr(vars['start_2'][period] >= vars[2][period] - vars[2][prev_period])
            model.addConstr(vars['start_3'][period] >= vars[3][period] - vars[3][prev_period])

    def _add_constraints_question_19(self,model,data,vars): 
        for depot in data['depots']:
            for factory in data['factories']:
                for customer in data['customers']:
                    model.addConstr(vars['factory_depot'][factory,depot] + vars['factory_customer'][factory,customer] <= data['factory_capacity'][factory])
            model.addConstr(sum(vars['factory_depot'][factory,depot] for factory in data['factories']) <= data['depot_capacity'][depot]) 
            # whatever we are serving to the customers from each depot that should not exceed the quantity we are getting from factories.  
            model.addConstr(sum(vars['depot_customer'][depot, customer] for customer in data['customers']) <= sum(vars['factory_depot'][factory,depot] for factory in data['factories']))
            # Demand constraint of customers

        for customer in data['customers']:
            model.addConstr((sum(vars['depot_customer'][d,customer] for d in data['depots']) + sum(vars['factory_customer'][f,customer] for f in data['factories'])) >= data['customer_demand'][customer])
            
            
            # preferrence constraint
            if data['preferred_suppliers'][customer] is not None:
                preferred = data['preferred_suppliers'][customer]

                # Sum of supply from all other factories
                sum_total= sum(vars['factory_customer'][f, customer] for f in data['factories']) + sum(vars['depot_customer'][d, customer] for d in data['depots'] )
                
            if isinstance(preferred, list):
                # for p in preferred:
                #     if p in data['factories']:
                #         model.addConstr(vars['factory_customer'][p, customer] + >= sum_other_factories + sum_other_depots)
                        model.addConstr(vars['depot_customer'][preferred[0], customer] + vars['depot_customer'][preferred[1], customer] >= 0.5*sum_total)
            else:
                if preferred in data['factories']:
                    model.addConstr(vars['factory_customer'][preferred, customer] >= 0.5*sum_total)
                else:    
                    model.addConstr(vars['depot_customer'][preferred, customer] >= 0.5*sum_total)
  