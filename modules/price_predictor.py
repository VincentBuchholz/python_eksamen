import prediction as pred
from motorregister import motor_register_interaction
from numberplate_detector import detect_numberplate
import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get a predicted price for your car')
    parser.add_argument('--image', help='path to image of car', required=True)
    
    args = parser.parse_args()
    
    numerplate = detect_numberplate(args.image)
    
    car_dict = motor_register_interaction(numerplate)
    
    df_detected = pd.DataFrame.from_dict(car_dict)
    
    #df_bilbasen,electric_car = pred.clean_data(pd.read_csv(f'../data/{df_detected['model']}_data.csv',sep=';'))
    
    #df_bilbasen
    
    #lr = pred.linear_reg(df_bilbasen,electric_car)
    
    #dtr = pred.decision_tree_reg(df_bilbasen,electric_car)
    
    print(df)
    