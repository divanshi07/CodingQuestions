class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        mergedArr=[]
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                mergedArr.append(nums1[i])
                i+=1
            else:
                mergedArr.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            mergedArr.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            mergedArr.append(nums2[j])
            j+=1
        left=0
        right=len(mergedArr)-1
        mid=left+(right-left)//2
        if(len(mergedArr)%2==0):
            median=(mergedArr[mid]+mergedArr[mid+1])/2
        elif(len(mergedArr)%2!=0):
            median = mergedArr[mid]
        return median 
        