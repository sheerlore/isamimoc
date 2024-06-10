import { onMounted, onUnmounted, ref } from "vue";

interface PoolingData {
    random: number
}

export function usePooling() {
    const data = ref<PoolingData | null>(null)
    let intervalId: number | null = null 

    const fetchData = async () => {
        try {
            const res = await fetch('http://localhost:8000/pooling/')
            const poolingData = await res.json()
            data.value = poolingData
        } catch (error) {
            console.error("Error Fetching Data: ", error)
        }
    }

    const startPooling = () => {
        intervalId = setInterval(fetchData, 5000)
    }

    const stopPooling = () => {
        if (intervalId) {
            clearInterval(intervalId)
        }
    }

    onMounted(startPooling)
    onUnmounted(stopPooling)
    return {
        data
    }
}