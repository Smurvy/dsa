public  class groupSumSolution{
  public boolean groupSum(int start, int[] nums, int target) {
    if (target == 0){
      return true;
    }
    
    if (start + 1 >  nums.length){
      return false;
    }
    if (groupSum(start + 1, nums, target - nums[start]) == false){
      return groupSum(start + 1, nums, target); 
    }
      
    else if (target - nums[start] >= 0) {
      return groupSum(start + 1, nums, target - nums[start]); 
    }
    return false;
  }

}

