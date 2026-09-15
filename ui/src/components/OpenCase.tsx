import { useState, type FormEvent } from "react";
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Alert,
  Box,
  Button,
  Container,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

type CaseField =
  | "scene_evidence"
  | "crime_report"
  | "records"
  | "security_log"
  | "suspects";

const caseFields: { key: CaseField; label: string; placeholder: string }[] = [
  {
    key: "scene_evidence",
    label: "Scene evidence",
    placeholder: "Describe the evidence found at the scene.",
  },
  {
    key: "crime_report",
    label: "Crime report",
    placeholder: "Enter the initial crime report.",
  },
  {
    key: "records",
    label: "Records",
    placeholder: "Add any relevant employee, financial, or other records.",
  },
  {
    key: "security_log",
    label: "Security log",
    placeholder: "Paste security logs or access records.",
  },
  {
    key: "suspects",
    label: "Suspects",
    placeholder: "List suspects and anything known about them.",
  },
];

const emptyCase = (): Record<CaseField, string> => ({
  scene_evidence: "",
  crime_report: "",
  records: "",
  security_log: "",
  suspects: "",
});

function OpenCase() {
  const [caseFiles, setCaseFiles] = useState(emptyCase);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string }>();

  async function submitCase(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsSubmitting(true);
    setMessage(undefined);

    try {
      const response = await fetch("http://localhost:8000/api/detective/create-case", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(caseFiles),
      });
      const content = (await response.json()) as { message?: string };

      if (!response.ok) {
        throw new Error(content.message ?? "Unable to create the case.");
      }

      setMessage({ type: "success", text: content.message ?? "Case created." });
      setCaseFiles(emptyCase());
    } catch (error) {
      setMessage({
        type: "error",
        text: error instanceof Error ? error.message : "Unable to create the case.",
      });
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <Container component="main" maxWidth="sm" sx={{ py: 4 }}>
      <Stack component="form" spacing={2} onSubmit={submitCase}>
        <Box>
          <Typography variant="h4" component="h1">
            Open a case
          </Typography>
        </Box>

        {caseFields.map(({ key, label, placeholder }) => (
          <Accordion key={key} disableGutters>
            <AccordionSummary>{label}</AccordionSummary>
            <AccordionDetails>
              <TextField
                fullWidth
                multiline
                minRows={6}
                label={label}
                placeholder={placeholder}
                value={caseFiles[key]}
                onChange={(event) =>
                  setCaseFiles((current) => ({ ...current, [key]: event.target.value }))
                }
              />
            </AccordionDetails>
          </Accordion>
        ))}

        {message && <Alert severity={message.type}>{message.text}</Alert>}

        <Button type="submit" variant="contained" disabled={isSubmitting}>
          {isSubmitting ? "Creating case…" : "Create case"}
        </Button>
      </Stack>
    </Container>
  );
}

export default OpenCase;
