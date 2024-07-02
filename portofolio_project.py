#First we need to import the csv file
import csv
#Then we will open the file 
with open('insurance.csv') as insurance_csv:
    #Then we will create empty lists to store the different type of values
    insurance_dict = list(csv.DictReader(insurance_csv))

    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    insurance_data = []
    for row in insurance_dict:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])
    #print(f'First three rows of the dataset:\n Age: {age[:3]}\n Sex: {sex[:3]}\n BMI: {bmi[:3]}\n Children: {children[:3]}\n Smoker: {smoker[:3]}\n Region: {region[:3]}\n Charges: {charges[:3]}')
    # 1. Here we create a function to calculate the average age of the patients(Mean age)
    def average_age(ages):
        total_ages = 0
        for row in ages:
            total_ages += int(row)
        return("The average age is : " + str(round(total_ages/len(ages)))) 
    print(average_age(age))
    # 2. Here we create a function to calculate how many males - females we have in our dataset
    def count_sexes(sexes):
        male = 0
        female = 0
        for row in sexes:
            if row == 'male':
                male+=1
            elif row == 'female':
                female+=1
        return('The number of males is: ' + str(male)+'\n' +'The number of females is: ' + str(female))
    print(count_sexes(sex))
    # 3. Here we create a function to calculate the average charge in the dataset
    def average_charge(charges):
        total_charge = 0
        for row in charges:
            total_charge+=float(row)
        return('The average charge of our dataset is: ' + str(round((total_charge/len(charges)), 2)))
    print(average_charge(charges))
    # 4. Here we create a function to calculate the average cost for males and females separately
    def gender_cost(insurance_dict):
        male_charges = 0
        female_charges = 0
        male_count = 0
        female_count = 0
 
        for row in insurance_dict:
            gender = row['sex']
            charges = float(row['charges'])
            if gender == 'male':
                male_charges+=charges
                male_count += 1
            elif gender == 'female':
                female_charges+=charges
                female_count += 1
        total_male_charges = male_charges/male_count
        total_female_charges = female_charges/female_count
        return('Average male charges: ' + str(round(total_male_charges, 2)) + '\nAverage female charges: '+ str(round( total_female_charges, 2)))
       
    print(gender_cost(insurance_dict))
    # 5. Here we will create a function to count the number of people living in the 4 different regions in our dataset
    def count_regions(insurance_dict):
        # Initialize a dictionary to count occurrences of each region
        region_counts = {}
        #reader = csv.DictReader(insurance_csv)
        #Iterate over each row in the file
        for row in insurance_dict:
            region = row['region']
            if region in region_counts:
                region_counts[region] +=1
            else:
                region_counts[region] = 1
        
        return region_counts
    print(count_regions(insurance_dict))
  

    # 6. Here we will create a function to calculate the avg cost between smokers and non smokers
    def smokers_cost(insurance_dict):
        smokers_count = 0
        non_smokers_count = 0
        smokers_total_cost = 0
        non_smokers_total_cost = 0
        for row in insurance_dict:
            smokers = row['smoker']
            charges = float(row['charges'])
            if smokers == 'yes':
                smokers_count +=1
                smokers_total_cost+=charges

            else:
                non_smokers_count +=1
                non_smokers_total_cost+=charges
        average_smoker_cost = smokers_total_cost/smokers_count
        average_non_smoker_cost = non_smokers_total_cost/non_smokers_count

        
        return('Number of smokers: '+ str(smokers_count) + '\nSmokers average cost:' + str(round(average_smoker_cost, 2)) + '\nNumber of non smokers: '+ str(non_smokers_count)+ '\nNon smokers average cost: ' + str(round(average_non_smoker_cost,2)))
    print(smokers_cost(insurance_dict))




    # 7. Here we will calculate the average charge of someone who has at least one child in our dataset
    def parent_cost(insurance_dict):
        parent_count = 0
        non_parent_count = 0
        parent_cost = 0
        non_parent_cost = 0
        for row in insurance_dict:
            children = row['children']
            charge = float(row['charges'])
            if children != '0':
                parent_count+=1
                parent_cost+=charge
            else:
                non_parent_count+=1
                non_parent_cost+=charge
        total_parent_cost = parent_cost/parent_count
        total_non_parent_cost = non_parent_cost/non_parent_count
        return('Number of people having at least one kid: '+ str(parent_count)+'\nNumber of people who do not have kid: '+ str(non_parent_count)+'\nAverage cost if someone has at least 1 kid: ' + str(round(total_parent_cost,2)) + '\nAverage cost if someone has not a kid: ' + str(round(total_non_parent_cost,2)) )
    print(parent_cost(insurance_dict))


    # 8. Here we will find the record with the lowest charge
    def lowest_charge(insurance_dict):
        lowest_charge = float('inf')
        lowest_charge_record = None
        for row in insurance_dict:
            charge = float(row['charges'])
            if charge < lowest_charge:
                lowest_charge = charge
                lowest_charge_record = row
        return ('The lowest record on the dataset: ' + str(lowest_charge_record))
    print(lowest_charge(insurance_dict))



    # 9. Here we will find the record with the highest charge
    def highest_charge(insurance_dict):
        highest_charge = float('-inf')
        highest_charge_record = None
        for row in insurance_dict:
            charge = float(row['charges'])
            if charge > highest_charge:
                highest_charge = charge
                highest_charge_record = row
        return('The highest record on the dataset: ' + str(highest_charge_record))
    print(highest_charge(insurance_dict))



