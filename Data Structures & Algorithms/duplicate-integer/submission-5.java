class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashset = new HashSet<Integer>();
        for(int i = 0; i<=nums.length-1;i++)
        {
            if(hashset.contains(nums[i]))
            {
                return true;
            }
            hashset.add(nums[i]);
        }
        return false;
    }
}
